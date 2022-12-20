# Structural Bioinformatics course by Carlo Camilloni
### Department of Biosciences, University of Milano, Italy

Structural Bioinformatics is an elective course for the master degrees in Molecular Biotecnology and Bioinformatics (MBB) and Quantitative Biology (QB). The aim is that of providing a general introduction to different computational approaches related to computational structural biology and biochemistry. This repository includes both the notes and the practicals. News about the course are published on the ARIEL web page.

### The main topics covered are:

1. Structures visualisation and analysis
2. Molecular Dynamics simulations (including QM)
3. Biomolecules Structure Prediction (including docking)

### The repository is organised as follow:

    Notes     : Slides of the lectures in PDF format
    Notebooks : Colab Notebooks for the practicals
    Data      : Additional files needed for the practicals

### Notes:
| Lecture |  Topic | Notes |
|:--------:|:-------------|:--------:|
| [![Generic badge](https://img.shields.io/badge/1-PDF-<COLOR>.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/01_StochasticMolecules.pdf) | A Statistical Mechanics view of Biomolecular Dynamics | Updated 2022 |
| [![Generic badge](https://img.shields.io/badge/2-PDF-<COLOR>.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/02_StructuralBiology.pdf) | Structural Biology and Structure Visualisation | Updated 2022 |
| [![Generic badge](https://img.shields.io/badge/3-PDF-<COLOR>.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/03_MolecularDynamics.pdf) | Molecular Dynamics simulations: force-fields, algorithms, analysis | Updated 2022 |
| [![Generic badge](https://img.shields.io/badge/4-PDF-<COLOR>.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/04_EnhancedMD.pdf) | Enhanced Sampling Techniques in MD | Updated 2022 |
| [![Generic badge](https://img.shields.io/badge/5-PDF-<COLOR>.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/05_MarkovSM.pdf) | Markov State Models (by [T. Giorgino](https://github.com/tonigi)) | Updated 2022 |
| [![Generic badge](https://img.shields.io/badge/6-PDF-<COLOR>.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/06_QM_MM_more.pdf) | Quantum Chemistry, QM/MM, and simplified models | Updated 2022 |
| [![Generic badge](https://img.shields.io/badge/7-PDF-<COLOR>.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/07_StructurePredictionDocking.pdf) | Structures Prediction and Molecular Docking | Updated 2022 |
| [![Generic badge](https://img.shields.io/badge/8-PDF-<COLOR>.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/08_MachineLearning.pdf) | Machine Learning (by [T. Giorgino](https://github.com/tonigi)) | Updated 2022 |
| [![Generic badge](https://img.shields.io/badge/9-PDF-<COLOR>.svg)](https://github.com/carlocamilloni/Structural-Bioinformatics/blob/main/Notes/09_Integrative_design.pdf) | Integrative Modelling and Protein Design | Updated 2022 |

### Practicals:

| Task | Notebook | Topic | Software |
|:--------:|:-------------:|:--------:|:------:|
| Lab.01 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/lab01_intro.ipynb) | Warm-up on Colab and Structures Visualisation | VMD |
| Lab.02 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/lab02_MD.ipynb) | Simple Molecular Dynamics simulations | GROMACS |
| Lab.03 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/lab02b_MDanalysis.ipynb) | More analysis of MD simulations | MDanalysis |
| Lab.04 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/lab03_MD_enhanced_martini.ipynb) | Enhanced sampling and simplified models | PLUMED, Martini |
| Lab.05 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/lab04_QM.ipynb) | Simple DFT simulations | CP2K |
| Lab.06 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/lab05_StructurePred.ipynb) | Protein Structure Prediction | psipred, ColabFold |
| Lab.07 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/lab06_docking.ipynb) | Molecular Docking | Autodock VINA |
| Lab.08 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlocamilloni/Structural-Bioinformatics/blob/main/Notebooks/Design.ipynb) | Protein Design | ColabDesign |

### Reference Papers:

1. **Seeing the PDB**: Richardson J.S., Richardson R.C., Goodsell D.S. (2021) J. Biol. Chem. 296:100742 https://doi.org/10.1016/j.jbc.2021.100742
2. **Biomolecular Simulation**: A Computational Microscope for Molecular Biology: Dror R.O., et al. (2012) Annu. Rev. Biophys. 41:429-452 https://doi.org/10.1146/annurev-biophys-042910-155245
3. (optional, learn more) **Unsupervised Learning Methods for Molecular Simulation Data**: Glielmo A., et al. (2021) Chem. Rev. 121:9722–9758 https://doi.org/10.1021/acs.chemrev.0c01195
4. (optional, learn more) **QM/MM Methods for Biomolecular Systems**: Senn H.M., Thiel W. (2009) Angew. Chem. Int. 48:1198–1229 https://doi.org/10.1002/anie.200802019
5. **Toward the solution of the protein structure prediction problem**: Pearce R., Zhang Y. (2021) J. Biol. Chem. 297:100870 https://doi.org/10.1002/anie.200802019
6. **Principles for Integrative Structural Biology Studies**: Rout P.M., Sali A. (2019) Cell 177:1384-1403 https://doi.org/10.1016/j.cell.2019.05.016
7. (optional, learn more) **Principles of protein structural ensemble determination**: Bonomi M., et al. (2017) Curr. Op. Struct. Biol. 42:106–116 http://dx.doi.org/10.1016/j.sbi.2016.12.004

### Exam:

The exam consists of a powerpoint presentation (max 10 minutes) of a scientific paper from a list provided below, this will be followed by few questions regarding the paper and the methodologies that we have dealt with in the lectures. Finally we will go through one of the Tasks performed in the lab by looking at the materials you produced.

Papers list: (TBA)
1. 
