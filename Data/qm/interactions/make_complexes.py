# Builds the starting structures of the new complexes (rigid-body fit of the two molecules with distance restraints).
# Then run optimise_complexes.py <name> (GFN2-xTB, then r2SCAN-3c with ORCA). Needs rdkit and scipy.
import os
import numpy as np, sys
from scipy.optimize import minimize
from scipy.spatial.transform import Rotation as Rot
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_complexes_place.py')).read().split('# ---------------- G-C')[0])   # helpers

def dock(elA, XA, elB, XB, restraints, seeds=40, rng=np.random.default_rng(0)):
    # restraints: list of (iA, iB, d0) ; rigid-body fit of B (6 DOF)
    cB = XB.mean(0); XB0 = XB - cB
    heavyA = np.array([e != 'H' for e in elA]); heavyB = np.array([e != 'H' for e in elB])
    polA = np.array([e in ('N', 'O') for e in elA]); polB = np.array([e in ('N', 'O') for e in elB])
    def coords(p):
        return Rot.from_rotvec(p[:3]).apply(XB0) + p[3:]
    def score(p):
        Y = coords(p); s = 0.0
        for i, j, d0 in restraints:
            s += 10 * (np.linalg.norm(XA[i] - Y[j]) - d0) ** 2
        d = np.linalg.norm(XA[:, None] - Y[None], axis=2)
        lim = np.where(heavyA[:, None] & heavyB[None], np.where(polA[:, None] & polB[None], 2.7, 3.1),
                       np.where(heavyA[:, None] | heavyB[None], 2.4, 2.1))
        # restrained pairs are allowed to be close
        for i, j, d0 in restraints:
            lim[i, j] = 0
        s += 20 * np.sum(np.clip(lim - d, 0, None) ** 2)
        return s
    best = None
    for k in range(seeds):
        p0 = np.concatenate([Rot.random(random_state=k).as_rotvec(), XA.mean(0) + rng.normal(0, 3, 3)])
        r = minimize(score, p0, method='Powell', options={'maxiter': 20000, 'xtol': 1e-4, 'ftol': 1e-6})
        if best is None or r.fun < best.fun:
            best = r
    print('  score', round(best.fun, 4))
    return coords(best.x)

out = {}
# G-C
mG, eG, XG, gm = mol3d('[O:6]=C1[NH:1]C([NH2:2])=NC2=C1N=CN2')
mC, eC, XC, cm = mol3d('[NH2:4]C1=[N:3]C(=[O:2])NC=C1')
H1 = hs_of(mG, gm[1])[0]; H21 = min(hs_of(mG, gm[2]), key=lambda h: np.linalg.norm(XG[h] - XG[gm[1]]))
H41 = min(hs_of(mC, cm[4]), key=lambda h: np.linalg.norm(XC[h] - XC[cm[3]]))
out['gc_wc'] = ('guanine-cytosine Watson-Crick', eG, XG, eC, dock(eG, XG, eC, XC, [(H1, cm[3], 1.9), (H21, cm[2], 1.9), (gm[6], H41, 1.9)]), 0, 0)
# DMS - benzene
mB, eB, XB, _ = mol3d('c1ccccc1'); Cs = [i for i, e in enumerate(eB) if e == 'C']
mS, eS, XS, sm = mol3d('C[S:1]C')
out['dms_benzene'] = ('dimethyl sulfide on benzene (Met-Phe)', eB, XB, eS, dock(eB, XB, eS, XS, [(c, sm[1], 4.0) for c in Cs]), 0, 0)
# methylammonium - 3-methylindole (above the six-membered ring)
mI, eI, XI, im = mol3d('Cc1c[nH]c2[cH:1][cH:2][cH:3][cH:4]c12')
ring6 = sorted(set([im[k] for k in (1, 2, 3, 4)] + [n.GetIdx() for k in (1, 4) for n in mI.GetAtomWithIdx(im[k]).GetNeighbors() if n.GetIsAromatic()]))
mA, eA, XA, am = mol3d('C[NH3+:1]')
out['methylammonium_indole'] = ('methylammonium on 3-methylindole (Lys-Trp cation-pi)', eI, XI, eA, dock(eI, XI, eA, XA, [(c, am[1], 3.4) for c in ring6]), 0, 1)
# acetate - methylguanidinium
mG2, eG2, XG2, g2 = mol3d('C[NH:1][C:3](=[NH2+:2])N')
mAc, eAc, XAc, ac = mol3d('C[C:3](=[O:1])[O-:2]')
Ha = hs_of(mG2, g2[1])[0]
Hb = min([h for a in mG2.GetAtoms() if a.GetSymbol() == 'N' and a.GetIdx() != g2[1] for h in hs_of(mG2, a.GetIdx())], key=lambda h: np.linalg.norm(XG2[h] - XG2[Ha]))
out['acetate_methylguanidinium'] = ('acetate - methylguanidinium (Asp-Arg salt bridge)', eAc, XAc, eG2,
                                    None, -1, 1)
XG2d = dock(eAc, XAc, eG2, XG2, [(ac[1], Ha, 1.75), (ac[2], Hb, 1.75)])
out['acetate_methylguanidinium'] = ('acetate - methylguanidinium (Asp-Arg salt bridge)', eAc, XAc, eG2, XG2d, -1, 1)
# NMA dimer
mN1, eN1, XN1, n1 = mol3d('C[C:2](=[O:1])[NH:3]C')
mN2, eN2, XN2, n2 = mol3d('C[C:2](=[O:1])[NH:3]C', seed=11)
Hn = hs_of(mN1, n1[3])[0]
out['nma_dimer'] = ('N-methylacetamide dimer (backbone N-H...O=C)', eN1, XN1, eN2, dock(eN1, XN1, eN2, XN2, [(Hn, n2[1], 1.95), (n1[3], n2[1], 2.95)]), 0, 0)
# dimethyl phosphate - methylguanidinium (Arg-phosphate, two N-H...O bonds to the two free O of the phosphate)
mP, eP, XP, pm = mol3d('CO[P:3](=[O:1])([O-:2])OC')
mG3, eG3, XG3, g3 = mol3d('C[NH:1][C:3](=[NH2+:2])N')
Ha3 = hs_of(mG3, g3[1])[0]
Hb3 = min([h for a in mG3.GetAtoms() if a.GetSymbol() == 'N' and a.GetIdx() != g3[1] for h in hs_of(mG3, a.GetIdx())], key=lambda h: np.linalg.norm(XG3[h] - XG3[Ha3]))
out['phosphate_methylguanidinium'] = ('dimethyl phosphate - methylguanidinium (Arg-DNA phosphate)', eP, XP, eG3, dock(eP, XP, eG3, XG3, [(pm[1], Ha3, 1.75), (pm[2], Hb3, 1.75)]), -1, 1)
# dimethyl phosphate - methylammonium (Lys-phosphate, one N-H...O bond)
mP2, eP2, XP2, pm2 = mol3d('CO[P:3](=[O:1])([O-:2])OC')
mA2, eA2, XA2, am2 = mol3d('C[NH3+:1]')
Hl = hs_of(mA2, am2[1])[0]
out['phosphate_methylammonium'] = ('dimethyl phosphate - methylammonium (Lys-DNA phosphate)', eP2, XP2, eA2, dock(eP2, XP2, eA2, XA2, [(pm2[1], Hl, 1.7), (pm2[1], am2[1], 2.7)]), -1, 1)
for name, (title, eA_, XA_, eB_, XB_, qA, qB) in out.items():
    if len(sys.argv) > 1 and name not in sys.argv[1:]:
        continue
    write(name, title, eA_, XA_, eB_, XB_, qA, qB)
