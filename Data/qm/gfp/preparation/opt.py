import numpy as np, subprocess, os, sys
O='/content/orca_6_1_1_linux_x86-64_shared_openmpi418_nodmrg/orca'; os.environ['OMP_NUM_THREADS']='1'
state=sys.argv[1]; q=0 if state=='neutral' else -1
L=open(f'../hbdi_gfp_{state}.xyz').read().splitlines(); n=int(L[0]); body=L[2:2+n]
X0=np.array([[float(v) for v in l.split()[1:4]] for l in body]); el=[l.split()[0] for l in body]
open(f'{state}.inp','w').write(f"""! r2SCAN-3c Opt TightSCF CPCM(water)
%geom
  Constraints
    {{D 2 3 4 5 C}}
    {{D 3 4 5 6 C}}
  end
end
* xyz {q} 1
""" + '\n'.join(body) + '\n*\n')
subprocess.run([O, f'{state}.inp'], stdout=open(f'{state}.out','w'), stderr=subprocess.STDOUT)
Y=np.array([[float(v) for v in l.split()[1:4]] for l in open(f'{state}.xyz').read().splitlines()[2:2+n]])
heavy=[i for i,e in enumerate(el) if e!='H']
P,Q=Y[heavy],X0[heavy]; pc,qc=P.mean(0),Q.mean(0); U,S,Vt=np.linalg.svd((P-pc).T@(Q-qc)); R=Vt.T@np.diag([1,1,np.sign(np.linalg.det(Vt.T@U.T))])@U.T
Z=(Y-pc)@R.T+qc
rmsd=np.sqrt(((Z[heavy]-X0[heavy])**2).sum(1).mean())
print(state, 'HURRAY' in open(f'{state}.out').read(), 'RMSD from the crystal (heavy atoms)', round(rmsd,3), 'C-O', round(np.linalg.norm(Z[8]-Z[9]),3))
head=L[1].replace('hydrogens optimised with GFN2-xTB','optimised with r2SCAN-3c in water (CPCM) keeping the two bridge dihedrals of the crystal, superposed on the crystal')
open(f'../hbdi_gfp_{state}.xyz','w').write(f'{n}\n{head}\n'+'\n'.join(f'{e:2s} {x:12.6f} {y:12.6f} {z:12.6f}' for e,(x,y,z) in zip(el,Z))+'\n')
