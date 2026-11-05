# Builds the RDKit/MMFF starting geometries of the chromophores of report 7, group 2: pip install rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import rdCIPLabeler
import os
mols = {
 # GFP chromophore model HBDI
 'hbdi_neutral': 'CC1=N/C(=C\\c2ccc(O)cc2)C(=O)N1C',
 'hbdi_anion':   'CC1=N/C(=C\\c2ccc([O-])cc2)C(=O)N1C',
 'hbdi_cation':  'CC1=[NH+]/C(=C\\c2ccc(O)cc2)C(=O)N1C',
 # protonated Schiff base (PSB) polyene models  H2C=CH-(CH=CH)n-CH=NH2+, the number is the number of conjugated double bonds
 'psb_2': 'C=C/C=[NH2+]',
 'psb_3': 'C=C/C=C/C=[NH2+]',
 'psb_4': 'C=C/C=C/C=C/C=[NH2+]',
 'psb_5': 'C=C/C=C/C=C/C=C/C=[NH2+]',
 'psb_6': 'C=C/C=C/C=C/C=C/C=C/C=[NH2+]',
 # retinal protonated Schiff base with methylamine
 'retinal_psb_alltrans': 'CC1=C(C(C)(C)CCC1)/C=C/C(C)=C/C=C/C(C)=C/C=[NH+]/C',
 'retinal_psb_11cis':    'CC1=C(C(C)(C)CCC1)/C=C/C(C)=C/C=C\\C(C)=C\\C=[NH+]\\C',
 # flavin
 'lumiflavin_ox':  'Cc1cc2nc3c(=O)[nH]c(=O)nc-3n(C)c2cc1C',
 'lumiflavin_red': 'Cc1cc2Nc3c(=O)[nH]c(=O)[nH]c3N(C)c2cc1C',
 # aromatic amino-acid side chains (Phe, Tyr, Trp) and tyrosinate
 'toluene':    'Cc1ccccc1',
 'p_cresol':   'Cc1ccc(O)cc1',
 'p_cresolate':'Cc1ccc([O-])cc1',
 '3_methylindole': 'Cc1c[nH]c2ccccc12',
}
out=os.path.dirname(os.path.abspath(__file__))
for name,smi in mols.items():
    m=Chem.AddHs(Chem.MolFromSmiles(smi))
    AllChem.EmbedMolecule(m, randomSeed=42)
    AllChem.MMFFOptimizeMolecule(m, maxIters=2000)
    q=Chem.GetFormalCharge(m)
    m2=Chem.RemoveHs(m); Chem.AssignStereochemistryFrom3D(m2); rdCIPLabeler.AssignCIPLabels(m2)
    st=[ (b.GetIdx(), b.GetPropsAsDict().get('_CIPCode')) for b in m2.GetBonds() if b.HasProp('_CIPCode')]
    conf=m.GetConformer()
    with open(f'{out}/{name}.xyz','w') as f:
        f.write(f"{m.GetNumAtoms()}\n{name} charge={q} multiplicity=1 SMILES={smi} (RDKit/MMFF starting geometry)\n")
        for a in m.GetAtoms():
            p=conf.GetAtomPosition(a.GetIdx()); f.write(f"{a.GetSymbol():2s} {p.x:12.6f} {p.y:12.6f} {p.z:12.6f}\n")
    print(f"{name:22s} N={m.GetNumAtoms():3d} q={q:+d} nelec={sum(a.GetAtomicNum() for a in m.GetAtoms())-q} stereo={st}")
