# Helper functions (and a first rough placement) used by make_complexes.py
import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem

def mol3d(smi, seed=7):
    m = Chem.AddHs(Chem.MolFromSmiles(smi))
    AllChem.EmbedMolecule(m, randomSeed=seed); AllChem.MMFFOptimizeMolecule(m, maxIters=5000)
    X = m.GetConformer().GetPositions()
    el = [a.GetSymbol() for a in m.GetAtoms()]
    maps = {a.GetAtomMapNum(): a.GetIdx() for a in m.GetAtoms() if a.GetAtomMapNum()}
    return m, el, X, maps

def hs_of(m, i):
    return [n.GetIdx() for n in m.GetAtomWithIdx(i).GetNeighbors() if n.GetSymbol() == 'H']

def kabsch(P, Q):
    # rotation R and translation t so that R@P_i + t ~ Q_i
    pc, qc = P.mean(0), Q.mean(0)
    H = (P - pc).T @ (Q - qc)
    U, S, Vt = np.linalg.svd(H)
    d = np.sign(np.linalg.det(Vt.T @ U.T))
    D = np.diag([1, 1, d])
    R = Vt.T @ D @ U.T
    return R, qc - R @ pc

def place(XB, idxB, targets):
    R, t = kabsch(XB[idxB], np.array(targets))
    return XB @ R.T + t

def unit(v): return v / np.linalg.norm(v)

def write(name, title, elA, XA, elB, XB, qA, qB):
    with open(f'{name}.xyz', 'w') as f:
        f.write(f'{len(elA)+len(elB)}\n{title} nA={len(elA)} nB={len(elB)} qA={qA} qB={qB}\n')
        for e, x in list(zip(elA, XA)) + list(zip(elB, XB)):
            f.write(f'{e:2s} {x[0]:10.4f} {x[1]:10.4f} {x[2]:10.4f}\n')
    print(name, len(elA)+len(elB))

# ---------------- G-C Watson-Crick (guanine 9H, cytosine 1H, as in the S22 A-T pair)
mG, eG, XG, gm = mol3d('[O:6]=C1[NH:1]C([NH2:2])=NC2=C1N=CN2')
mC, eC, XC, cm = mol3d('[NH2:4]C1=[N:3]C(=[O:2])NC=C1')
# make guanine planar-ish frame: fine (MMFF is planar)
H1 = hs_of(mG, gm[1])[0]
H2s = hs_of(mG, gm[2]); H21 = min(H2s, key=lambda h: np.linalg.norm(XG[h] - XG[gm[1]]))
O6 = gm[6]; C6 = [n.GetIdx() for n in mG.GetAtomWithIdx(O6).GetNeighbors()][0]
H4s = hs_of(mC, cm[4]); H41 = min(H4s, key=lambda h: np.linalg.norm(XC[h] - XC[cm[3]]))
tN3 = XG[H1] + 1.95 * unit(XG[H1] - XG[gm[1]])
tO2 = XG[H21] + 1.90 * unit(XG[H21] - XG[gm[2]])
tH41 = XG[O6] + 1.90 * unit(XG[O6] - XG[C6])
XCp = place(XC, [cm[3], cm[2], H41], [tN3, tO2, tH41])
write('gc_wc', 'guanine-cytosine Watson-Crick', eG, XG, eC, XCp, 0, 0)

# ---------------- dimethyl sulfide on benzene (Met-Phe, S-pi)
mB, eB, XB0, _ = mol3d('c1ccccc1')
c = XB0[[i for i, e in enumerate(eB) if e == 'C']].mean(0); XB0 -= c
n = unit(np.cross(XB0[0] - XB0[1], XB0[0] - XB0[2])) if False else None
Cs = [i for i, e in enumerate(eB) if e == 'C']
n = unit(np.cross(XB0[Cs[0]], XB0[Cs[2]]))
mS, eS, XS, sm = mol3d('C[S:1]C')
S = sm[1]; Cm = [i for i, e in enumerate(eS) if e == 'C']
mid = XS[Cm].mean(0); h = np.linalg.norm(mid - XS[S]); half = np.linalg.norm(XS[Cm[0]] - XS[Cm[1]]) / 2
xax = unit(XB0[Cs[0]] - np.dot(XB0[Cs[0]], n) * n)
tS = 3.7 * n
tC1 = tS + h * n + half * xax; tC2 = tS + h * n - half * xax
XSp = place(XS, [S, Cm[0], Cm[1]], [tS, tC1, tC2])
write('dms_benzene', 'dimethyl sulfide on benzene (Met-Phe)', eB, XB0, eS, XSp, 0, 0)

# ---------------- methylammonium on 3-methylindole, above the six-membered ring (Lys-Trp cation-pi)
mI, eI, XI, im = mol3d('Cc1c[nH]c2[cH:1][cH:2][cH:3][cH:4]c12')
ring6 = [im[k] for k in (1, 2, 3, 4)]
ring6 += [n.GetIdx() for k in (1, 4) for n in mI.GetAtomWithIdx(im[k]).GetNeighbors() if n.GetIsAromatic() and n.GetIdx() not in ring6]
ring6 = sorted(set(ring6))
cen = XI[ring6].mean(0)
nI = unit(np.cross(XI[ring6[0]] - cen, XI[ring6[2]] - cen))
mA, eA, XA, am = mol3d('C[NH3+:1]')
N = am[1]; HN = hs_of(mA, N); Cme = [i for i, e in enumerate(eA) if e == 'C'][0]
# N above the ring centre at 3.0 A, C-N axis along the normal (one ring-pointing H is not needed: the three N-H point down)
tN = cen + 3.0 * nI; tC = tN + np.linalg.norm(XA[Cme] - XA[N]) * nI
perp = unit(np.cross(nI, [1, 0, 0]))
Hd = XA[HN[0]] - XA[N]; along = np.dot(Hd, unit(XA[N] - XA[Cme])); radial = np.sqrt(np.dot(Hd, Hd) - along**2)
tH = tN - along * nI * -1 + radial * perp  # H below N (towards the ring)
tH = tN + along * nI + radial * perp
XAp = place(XA, [N, Cme, HN[0]], [tN, tC, tH])
write('methylammonium_indole', 'methylammonium on 3-methylindole (Lys-Trp cation-pi)', eI, XI, eA, XAp, 0, 1)

# ---------------- acetate - methylguanidinium (Asp-Arg salt bridge, two parallel N-H...O bonds)
mG2, eG2, XG2, g2 = mol3d('C[NH:1][C:3](=[NH2+:2])N')
mAc, eAc, XAc, ac = mol3d('C[C:3](=[O:1])[O-:2]')
Ha = hs_of(mG2, g2[1])[0]
Hb = min(hs_of(mG2, g2[2]), key=lambda h: np.linalg.norm(XG2[h] - XG2[Ha]))
tO1 = XG2[Ha] + 1.75 * unit(XG2[Ha] - XG2[g2[1]])
tO2 = XG2[Hb] + 1.75 * unit(XG2[Hb] - XG2[g2[2]])
midO = (tO1 + tO2) / 2; midH = (XG2[Ha] + XG2[Hb]) / 2
hC = np.linalg.norm(XAc[ac[3]] - (XAc[ac[1]] + XAc[ac[2]]) / 2)
tCc = midO + hC * unit(midO - midH)
XAcp = place(XAc, [ac[1], ac[2], ac[3]], [tO1, tO2, tCc])
write('acetate_methylguanidinium', 'acetate - methylguanidinium (Asp-Arg salt bridge)', eAc, XAcp, eG2, XG2, -1, 1)

# ---------------- N-methylacetamide dimer (backbone N-H...O=C)
mN1, eN1, XN1, n1 = mol3d('C[C:2](=[O:1])[NH:3]C')
mN2, eN2, XN2, n2 = mol3d('C[C:2](=[O:1])[NH:3]C', seed=11)
Hn = hs_of(mN1, n1[3])[0]
u = unit(XN1[Hn] - XN1[n1[3]])
tO = XN1[Hn] + 1.95 * u
tC = tO + 1.23 * u
# third point: N of molecule 2 in the plane of molecule 1, on the side of its carbonyl
plane_n = unit(np.cross(XN1[n1[2]] - XN1[n1[3]], XN1[n1[1]] - XN1[n1[3]]))
side = unit(np.cross(plane_n, u))
dCN = np.linalg.norm(XN2[n2[3]] - XN2[n2[2]])
tNn = tC + dCN * unit(0.5 * u + 0.87 * side)
XN2p = place(XN2, [n2[1], n2[2], n2[3]], [tO, tC, tNn])
write('nma_dimer', 'N-methylacetamide dimer (backbone N-H...O=C)', eN1, XN1, eN2, XN2p, 0, 0)

# ---------------- methanol - acetate (Ser-Asp, charge-assisted O-H...O)
mM, eM, XM, mm = mol3d('C[OH:1]')
mAc2, eAc2, XAc2, ac2 = mol3d('C[C:3](=[O:1])[O-:2]')
Ho = hs_of(mM, mm[1])[0]; u = unit(XM[Ho] - XM[mm[1]])
tO1 = XM[Ho] + 1.65 * u
tCc = tO1 + 1.26 * unit(u + 0.6 * unit(np.cross(u, [0, 0, 1])))
dOO = np.linalg.norm(XAc2[ac2[1]] - XAc2[ac2[2]])
tO2 = tCc + 1.26 * unit(tCc - tO1 + 0.3 * unit(np.cross(u, [0, 1, 0])))
XAc2p = place(XAc2, [ac2[1], ac2[3], ac2[2]], [tO1, tCc, tO2])
write('methanol_acetate', 'methanol - acetate (Ser-Asp, charge-assisted H-bond)', eM, XM, eAc2, XAc2p, 0, -1)
