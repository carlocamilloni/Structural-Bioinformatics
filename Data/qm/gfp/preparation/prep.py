import numpy as np, subprocess, os, re
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Geometry import Point3D
O='/content/orca_6_1_1_linux_x86-64_shared_openmpi418_nodmrg/orca'; os.environ['OMP_NUM_THREADS']='1'
# crystal coordinates of the chromophore
cro={}
for l in open('1EMA.pdb'):
    if l.startswith('HETATM') and l[17:20]=='CRO':
        cro[l[12:16].strip()]=np.array([float(l[30:38]),float(l[38:46]),float(l[46:54])])
# HBDI with atom maps = CRO atom names
names={1:'CA1',2:'C1',3:'N2',4:'CA2',5:'CB2',6:'CG2',7:'CD1',8:'CE1',9:'CZ',10:'OH',11:'CE2',12:'CD2',13:'C2',14:'O2',15:'N3',16:'CA3'}
smi={'neutral':'[CH3:1][C:2]1=[N:3]/[C:4](=[CH:5]\\[c:6]2[cH:7][cH:8][c:9]([OH:10])[cH:11][cH:12]2)[C:13](=[O:14])[N:15]1[CH3:16]',
     'anion':  '[CH3:1][C:2]1=[N:3]/[C:4](=[CH:5]\\[c:6]2[cH:7][cH:8][c:9]([O-:10])[cH:11][cH:12]2)[C:13](=[O:14])[N:15]1[CH3:16]'}
for state,s in smi.items():
    m=Chem.AddHs(Chem.MolFromSmiles(s))
    cmap={a.GetIdx():Point3D(*cro[names[a.GetAtomMapNum()]]) for a in m.GetAtoms() if a.GetAtomMapNum()}
    AllChem.EmbedMolecule(m, randomSeed=1); AllChem.MMFFOptimizeMolecule(m)
    conf=m.GetConformer()
    heavy=list(cmap)
    # align the embedded molecule on the crystal heavy atoms, then put the heavy atoms exactly at the crystal positions
    from rdkit.Chem import rdMolAlign
    rdMolAlign.AlignMol(m, m, atomMap=[(i,i) for i in heavy])  # no-op, keep
    P=np.array([list(conf.GetAtomPosition(i)) for i in heavy]); Q=np.array([list(cmap[i]) for i in heavy])
    pc,qc=P.mean(0),Q.mean(0); U,S,Vt=np.linalg.svd((P-pc).T@(Q-qc)); R=Vt.T@np.diag([1,1,np.sign(np.linalg.det(Vt.T@U.T))])@U.T
    X=(np.array(conf.GetPositions())-pc)@R.T+qc
    for i in heavy: X[i]=list(cmap[i])
    el=[a.GetSymbol() for a in m.GetAtoms()]
    q=Chem.GetFormalCharge(m)
    # optimise only the hydrogens with GFN2-xTB (heavy atoms fixed at the crystal positions)
    cons='\n'.join(f'    {{C {i} C}}' for i in heavy)
    blk='\n'.join(f'{e} {x:.4f} {y:.4f} {z:.4f}' for e,(x,y,z) in zip(el,X))
    os.makedirs(state,exist_ok=True)
    open(f'{state}/h.inp','w').write(f'! Native-GFN2-XTB Opt\n%geom\n  Constraints\n{cons}\n  end\nend\n* xyz {q} 1\n{blk}\n*\n')
    subprocess.run([O,'h.inp'],cwd=state,stdout=open(f'{state}/h.out','w'),stderr=subprocess.STDOUT)
    L=open(f'{state}/h.xyz').read().splitlines()
    n=int(L[0]); Y=np.array([[float(v) for v in l.split()[1:4]] for l in L[2:2+n]])
    print(state, 'charge', q, 'atoms', n, 'max heavy-atom shift', np.abs(Y[heavy]-X[heavy]).max().round(3), 'TERMINATED' in open(f'{state}/h.out').read())
    open(f'hbdi_gfp_{state}.xyz','w').write(f'{n}\nHBDI ({state}) at the geometry of the chromophore in GFP S65T (PDB 1EMA), hydrogens optimised with GFN2-xTB charge={q}\n'+'\n'.join(L[2:2+n])+'\n')
