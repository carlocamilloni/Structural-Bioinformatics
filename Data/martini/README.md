# Martini 3 files for T06 (lipid bilayers)

| File | Content | Source |
|:--|:--|:--|
| `martini_v3.0.0.itp` | Martini 3 bead types and non-bonded interactions | Souza et al., Nat. Methods 18:382 (2021) |
| `martini_v3.0.0_ffbonded_v2.itp`, `martini_v3.0.0_phospholipids_PC_v2.itp` | refined Martini 3 lipid parameters (bonded types must be included before the lipids) | Pedersen et al., ACS Cent. Sci. (2025), https://doi.org/10.1021/acscentsci.5c00755 |
| `martini_v3.0.0_sterols_v1.itp` | Martini 3 cholesterol | Borges-Araújo et al., JCTC 19:7387 (2023) |
| `martini_v3.0.0_solvents_v1.itp`, `martini_v3.0.0_ions_v1.itp` | water (`W`, 4 water molecules per bead) and ions (`NA`, `CL`) | Souza et al. (2021) |
| `insane.py` | insane, Martini 3 lipid version (`tools/insane_M3_lipids_new.py`) | Wassenaar et al., JCTC 11:2144 (2015) |
| `benchmark/figure1_*_data.csv` | experimental and simulated (Martini 3) area per lipid (`apl`), thicknesses (`dhh`, `db`, `2dc`) | Pedersen et al. (2025) |
| `martini_lipids.top` | topology header including all the files above | this course |
| `martini_*.mdp` | minimisation, self-assembly, equilibration and production parameters | this course |
| `DPPC-single.gro`, `water.gro` | one DPPC molecule, a box of Martini water | this course |

The lipid, cholesterol, insane and benchmark files come from
https://github.com/Martini-Force-Field-Initiative/M3-Lipid-Parameters (commit 2121527, Apache 2.0 license, see `LICENSE_M3-Lipid-Parameters.txt`).
