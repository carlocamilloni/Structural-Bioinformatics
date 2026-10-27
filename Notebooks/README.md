### Getting started

All practicals run as Google Colab notebooks, so no local installation is required — just a Google account. Click any "Open in Colab" badge below to launch a notebook directly.

#### Running locally (optional)

If you prefer to work on your own computer (Linux, macOS, or Windows through [WSL](https://learn.microsoft.com/windows/wsl/)), install [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) (or [miniforge](https://github.com/conda-forge/miniforge)), download or clone this repository, and from its main folder run:

    conda env create -f environment.yml
    conda activate sb
    jupyter lab

Then open the notebook from the `Notebooks` folder. Notes:

* The environment currently covers **T00** (`t00_intro.ipynb`, `report_00.ipynb`) , **T02** (`t02_StructurePred.ipynb`: the analysis and the S4PRED secondary structure prediction; the structure predictions themselves are run on servers and GPUs), **T03** (docking), **T04** (`t04_MD.ipynb`, `report_4_MD.ipynb`), **T05** (`t05_MDanalysis.ipynb`, `report_5_MDanalysis.ipynb`) and **T06** (`t06_MD_enhanced_martini.ipynb`, `report_6_MD_enhanced_martini.ipynb`: GROMACS with PLUMED). On your computer GROMACS runs on the CPU, so the simulations of T04 are much slower than on a Colab GPU: plan shorter runs or use Colab for them. The other practicals rely on software that is installed inside Colab (e.g. CP2K) and will be added to the environment progressively; until then please use Colab for them. [VMD](https://www.ks.uci.edu/Research/vmd/) is needed for T01.
* The cells that use Google Colab features (for example mounting Google Drive) can be skipped locally.
* Notebooks write their output files in a folder next to the notebook (for example `Task2/`), which is ignored by git.
* To update the environment after a `git pull`: `conda env update -f environment.yml --prune`.
