# Structural Bioinformatics

**Carlo Camilloni, Department of Biosciences, University of Milano, Italy**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/t01_VMD.pdf)

Structural Bioinformatics is an elective course offered within the Master's programmes in Molecular Biotechnology and Bioinformatics (MBB) and Quantitative Biology (QB). The course introduces a range of computational approaches for modeling and designing biomolecular structures, dynamics, and functions. This repository provides both lecture notes and laboratory exercises, while course updates and announcements will be posted on the [ARIEL platform](https://ariel.unimi.it/).

### The main topics covered are:

1. Structures visualisation and analysis
2. Biomolecules structure prediction
3. Molecular dynamics simulations
4. Integrative modelling and protein design

### Getting started

All practicals run as Google Colab notebooks, so no local installation is required — just a Google account. Click any "Open in Colab" badge below to launch a notebook directly.
You will also need [VMD](https://www.ks.uci.edu/Research/vmd/) or [ChimeraX](https://www.cgl.ucsf.edu/chimerax/).

If you want to run notebooks locally check the [README.md](Notebooks/README.md) file in the notebooks folder.

### Repository structure

    Notes     : Slides of the lectures in PDF format
    Notebooks : Colab Notebooks for the practicals (t0X_*.ipynb) and their report templates (report_X_*.ipynb)
    Data      : Additional input files needed for the practicals
        docking/ : protein and ligand structures for the docking exercise (T03)
        martini/ : Martini coarse-grained force field and topology files (T06)
        md/      : GROMACS .mdp parameter files and PLUMED metadynamics inputs (T04–T06)
        qm/      : small-molecule structures and reference output for the QM exercise (T07)
        stats/   : datasets for the statistical analysis exercise (T00)

For each academic year, a snapshot of the repository is saved as a release/tag (see [Previous years](#previous-years) below).

### Academic year 2026-2027

| # | Topic | Slides | Notes | Last Updated |
|:--:|:-------------|:--------:|:--------:|:--------:|
| 0 | Introduction: information about the course | [![Generic badge](https://img.shields.io/badge/PDF-lightgrey.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/00_Intro.pdf) | | 09/2026 |
| 1 | Structural Biology beyond static structures | [![Generic badge](https://img.shields.io/badge/PDF-blue.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/01_StructuralBiology.pdf) | [![Generic badge](https://img.shields.io/badge/PDF-blue.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/01_StructuralBiology_notes.pdf) | 09/2026 |
| 2 | A Statistical Mechanics view of Biomolecular Dynamics | [![Generic badge](https://img.shields.io/badge/PDF-blue.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/02_StochasticMolecules.pdf) | [![Generic badge](https://img.shields.io/badge/PDF-blue.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/02_StochasticMolecules_notes.pdf) | 10/2026 |
| 3 | Machine Learning (by [T. Giorgino](https://github.com/giorginolab)) | [![Generic badge](https://img.shields.io/badge/PDF-blue.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/03_MachineLearning.pdf) | | 10/2025 |
| 4 | Structures Prediction and Molecular Docking | [![Generic badge](https://img.shields.io/badge/PDF-blue.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/04_StructurePredictionDocking.pdf) | | 10/2025 |
| 5 | Molecular Dynamics simulations: force-fields, algorithms, analysis | [![Generic badge](https://img.shields.io/badge/PDF-blue.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/05_MolecularDynamics.pdf) | | 11/2025 |
| 6 | Enhanced Sampling Techniques in MD | [![Generic badge](https://img.shields.io/badge/PDF-blue.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/06_EnhancedMD.pdf) | | 11/2025 |
| 7 | Markov State Models (by [T. Giorgino](https://github.com/giorginolab)) | [![Generic badge](https://img.shields.io/badge/PDF-blue.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/07_MarkovSM.pdf) | | 11/2025 |
| 8 | Quantum Chemistry, QM/MM, and simplified models | [![Generic badge](https://img.shields.io/badge/PDF-blue.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/08_QM_MM_more.pdf) | | 12/2025 |
| 9 | Integrative Modelling and Protein Design | [![Generic badge](https://img.shields.io/badge/PDF-blue.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/09_Integrative_design.pdf) | | 12/2025 |

### Practicals

| Task | Instructions | Report | Last Updated |
|:--------|:-------------:|:-------------:|:------:|
| T00: Introduction to Colab and Statistics Practicals | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/t00_intro.ipynb) | | 10/2026 |
| T01: Biomolecular Structures Visualisation | [![Generic badge](https://img.shields.io/badge/PDF-lightgrey.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/t01_VMD.pdf) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/report_1_visual.ipynb) | 10/2026 |
| T02: Protein Structure Prediction | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/t02_StructurePred.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/report_2_StructurePred.ipynb) | 10/2026 |
| T03: Molecular Docking | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/t03_docking.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/report_3_docking.ipynb) | 10/2026 |
| T04: Molecular Dynamics simulations | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/t04_MD.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/report_4_MD.ipynb) | 10/2025 |
| T05: More on the analysis of MD simulations | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/t05_MDanalysis.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/report_5_MDanalysis.ipynb) | 11/2025 |
| T06: Enhanced sampling and simplified models | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/t06_MD_enhanced_martini.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/report_6_MD_enhanced_martini.ipynb) | 11/2025 |
| T07: Basic DFT simulations | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/t07_QM.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/report_7_QM.ipynb) | 11/2025 |
| T08: Protein Design | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/t08_design.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/report_8_design.ipynb) | 11/2025 |

### Reference Papers

The following publications are to be considered as part of the course and should be read before the exam.

1. **Seeing the PDB**: Richardson J.S., Richardson R.C., Goodsell D.S. (2021) J. Biol. Chem. 296:100742. https://doi.org/10.1016/j.jbc.2021.100742
2. **Biomolecular Simulation: A Computational Microscope for Molecular Biology**: Dror R.O., et al. (2012) Annu. Rev. Biophys. 41:429-452. https://doi.org/10.1146/annurev-biophys-042910-155245
3. **Toward the solution of the protein structure prediction problem**: Pearce R., Zhang Y. (2021) J. Biol. Chem. 297:100870. https://doi.org/10.1016/j.jbc.2021.100870

### Exam

The exam consists of a PowerPoint presentation (max 10 minutes) of a scientific paper from the list below, followed by a few questions on the paper and the methods we have covered in the lectures. Lab reports will also contribute to the final grade. See the introductory slide above for more information.

List of papers (academic year 2026/2027):
To be announced 

### Previous years

Each past edition of the course is preserved as a git tag:
- [2022/2023](https://github.com/carlocamilloni/Structural-Bioinformatics/tree/2022/2023)
- [2023/2024](https://github.com/carlocamilloni/Structural-Bioinformatics/tree/2023/2024)
- [2024/2025](https://github.com/carlocamilloni/Structural-Bioinformatics/tree/2024/2025)
- [2025/2026](https://github.com/carlocamilloni/Structural-Bioinformatics/tree/2025/2026)

### License & contact

This repository is released under the [MIT License](LICENSE). For questions about the course, please use the ARIEL platform's discussion board or contact Carlo Camilloni directly.
