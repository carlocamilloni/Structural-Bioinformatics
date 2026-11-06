# GFP (PDB 1EMA, S65T mutant) for report 7, group 2

Files used by `Notebooks/report_7_QM.ipynb`:

* `hbdi_gfp_anion.xyz`, `hbdi_gfp_neutral.xyz`: the QM part, the conjugated part of the chromophore (residue CRO 66) capped with
  methyl groups where it joins the backbone, i.e. HBDI. Optimised with r2SCAN-3c in water (CPCM) keeping the two bridge dihedrals
  of the crystal, and superposed on the crystal heavy atoms (RMSD 0.13 Å). The crystal geometry itself has a too-long phenolate C–O
  bond (1.48 Å), which gives a spurious dark state.
* `gfp_anion.pc`, `gfp_neutral.pc`: ORCA point-charge files (number of charges, then `q x y z` in Å) with the AMBER charges of all the
  protein atoms and of the 95 crystal waters (TIP3P).
* `gfp_*_charges.csv`: the same charges with residue names, numbers and atom names (used for the virtual mutations).
* `gfp_protein.pdb`: the protein with hydrogens, for the pictures.

Preparation (`preparation/`):
1. MSE → MET, chromophore removed; `pdb2pqr --ff=AMBER --ffout=AMBER --titration-state-method=propka --with-ph=7.0 --keep-chain`
   (pdb2pqr 3.8 / propka). propka makes Glu222 neutral (GLH) and His148 HID: this is the version for the anionic chromophore.
2. Neutral chromophore: Glu222 charged (charges of another Glu of the protein) and His148 as HIE (H on NE2), so that the phenol O–H
   can point to His148.
3. The charges of C, O of Phe64 and N, H of Val68 (bonded to the chromophore) are set to zero and moved to the CA of the same residue.
4. `prep.py` builds HBDI on the crystal coordinates (RDKit, hydrogens optimised with GFN2-xTB); `opt.py` optimises it as described above.
