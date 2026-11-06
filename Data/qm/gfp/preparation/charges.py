import numpy as np, csv
def read_pqr(f):
    rows=[]
    for l in open(f):
        if l.startswith(('ATOM','HETATM')):
            p=l.split()
            rows.append(dict(atom=p[2], resname=p[3], chain=p[4], resid=int(p[5]), x=float(p[6]), y=float(p[7]), z=float(p[8]), q=float(p[9])))
    return rows
B=read_pqr('gfp_A.pqr')     # propka: Glu222 neutral (GLH) -> state with the anionic chromophore
# charges of a standard (charged) Glu, from another Glu of the same protein
glu=[r for r in B if r['resname']=='GLU']
ref_id=glu[0]['resid']; gq={r['atom']:r['q'] for r in glu if r['resid']==ref_id}
# His148: with the neutral chromophore the phenol O-H needs the N of His148, so His148 takes the other tautomer (HIE: H on NE2)
hie=[r for r in B if r['resname']=='HIE']; hid=hie[0]['resid']; hq={r['atom']:r['q'] for r in hie if r['resid']==hid}
h148={r['atom']:np.array([r['x'],r['y'],r['z']]) for r in B if r['resid']==148}
u=(h148['NE2']-h148['CD2'])+(h148['NE2']-h148['CE1']); he2=h148['NE2']+1.01*u/np.linalg.norm(u)
A=[]
for r in B:
    r=dict(r)
    if r['resid']==222:
        if r['atom']=='HE2': continue
        r['resname']='GLU'; r['q']=gq[r['atom']]
    if r['resid']==148:
        if r['atom']=='HD1':
            r.update(atom='HE2', x=he2[0], y=he2[1], z=he2[2])
        r['resname']='HIE'; r['q']=hq[r['atom']]
    A.append(r)
def fix_boundary(rows):
    # the backbone atoms bonded to the chromophore (C, O of Phe64; N, H of Val68) are switched off;
    # their charge is moved to the CA of the same residue, so that every residue keeps its total charge
    rows=[dict(r) for r in rows]
    for resid, atoms in [(64, ('C','O')), (68, ('N','H'))]:
        moved=sum(r['q'] for r in rows if r['resid']==resid and r['atom'] in atoms)
        for r in rows:
            if r['resid']==resid and r['atom'] in atoms: r['q']=0.0
        for r in rows:
            if r['resid']==resid and r['atom']=='CA': r['q']+=moved
    return rows
for state, rows, xyz in [('anion', B, 'hbdi_gfp_anion.xyz'), ('neutral', A, 'hbdi_gfp_neutral.xyz')]:
    rows=fix_boundary(rows)
    L=open(xyz).read().splitlines(); n=int(L[0]); X=np.array([[float(v) for v in l.split()[1:4]] for l in L[2:2+n]])
    P=np.array([[r['x'],r['y'],r['z']] for r in rows])
    d=np.linalg.norm(P[:,None]-X[None],axis=2).min(1)
    tot=sum(r['q'] for r in rows)
    print(state, 'point charges', len(rows), 'total MM charge', round(tot,3), 'closest MM atom to the QM region', round(d.min(),2), 'Å', [ (rows[i]['resname'],rows[i]['resid'],rows[i]['atom'],round(d[i],2)) for i in np.argsort(d)[:4]])
    with open(f'gfp_{state}.pc','w') as f:
        f.write(f'{len(rows)}\n'+''.join(f"{r['q']:9.4f} {r['x']:9.3f} {r['y']:9.3f} {r['z']:9.3f}\n" for r in rows))
    with open(f'gfp_{state}_charges.csv','w',newline='') as f:
        w=csv.DictWriter(f, fieldnames=['resname','chain','resid','atom','q','x','y','z']); w.writeheader(); w.writerows([{k:r[k] for k in ['resname','chain','resid','atom','q','x','y','z']} for r in rows])
