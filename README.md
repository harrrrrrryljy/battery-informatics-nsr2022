# Battery Informatics: LDM Database Engineering (NSR 2022)

This repository contains the data processing pipeline and feature engineering protocols developed for our study published in **National Science Review (2022)**.

## 📌 Overview
The core of this project is the construction of **Local Density Models (LDMs)** to investigate battery interphase evolution. We transitioned from raw, unstructured atomistic trajectories to structured physical descriptors suitable for informatics analysis.

## 🛠 Key Contributions (AI4S Focused)
- **Data Curation Pipeline:** Automated extraction and cleaning of large-scale [AIMD](https://en.wikipedia.org) trajectories (VASP output parsing).
- **Feature Engineering:** Developed physics-constrained descriptors (e.g., local coordination density) to represent disordered chemical environments.
- **Data Integrity:** Implemented robust filtering algorithms to eliminate non-physical artifacts from [DFT](https://en.wikipedia.org) calculation noise.

## 📄 Related Publication
*S. N. Li, ..., **J. Y. Li**, et al. "Title of your NSR Paper," **National Science Review**, 2022.*
[Link to Paper]

## 💻 Tech Stack
- **Language:** Python 3.8+
- **Libraries:** [Pandas](https://pandas.pydata.org), [NumPy](https://numpy.org), [Matplotlib](https://matplotlib.org), [SciPy](https://scipy.org)
