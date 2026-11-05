# Builds the S22 / S22x5 dimers (xyz) and their CCSD(T)/CBS reference interaction energies (kcal/mol) from ASE: pip install ase
import csv, os
from ase.data import s22
from ase.units import kcal, mol
EV2KCAL = 1/(kcal/mol)
out=os.path.dirname(os.path.abspath(__file__))
rows=[]
for i,name in enumerate(s22.s22, start=1):
    d=s22.data[name]
    nA,nB=d['dimer atoms']
    for f in ['0.9','1.0','1.2','1.5','2.0']:
        pos=d['positions '+f]
        e = s22.get_interaction_energy_s22x5(name, float(f)) if f!='1.0' else s22.get_interaction_energy_cc(name)
        e*=EV2KCAL
        fn=f"{i:02d}_{name}_{f}.xyz"
        with open(os.path.join(out,fn),'w') as fh:
            fh.write(f"{len(pos)}\nS22 #{i} {name} scale={f} nA={nA} nB={nB} Eint_ref={e:.3f} kcal/mol\n")
            for s,p in zip(d['symbols'],pos):
                fh.write(f"{s:2s} {p[0]:12.6f} {p[1]:12.6f} {p[2]:12.6f}\n")
        rows.append(dict(id=i,system=name,scale=f,nA=nA,nB=nB,Eint_ref_kcal=round(e,3),file=fn,description=d['description']))
with open(os.path.join(out,'s22x5_reference.csv'),'w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
