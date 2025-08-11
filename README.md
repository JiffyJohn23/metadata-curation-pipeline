# Metadata Curation Pipeline

**Mini project:** metadata harmonization for public bioinformatics datasets (GEO, SRA, HCA, CellXGene).

## Overview
This repository contains a small, runnable metadata curation pipeline implemented in Python (Jupyter notebook + script). It standardizes fields such as `sex`, `species`, `age`, and `disease_summary`, applies controlled vocabularies, and preserves original values for traceability.

## Contents
- `notebooks/metadata_curation.ipynb` — documented notebook walkthrough (example run).
- `scripts/curate_metadata.py` — CLI script to run data curation on a CSV.
- `data/sample_metadata.csv` — small sample dataset (safe, scrubbed).
- `requirements.txt` — Python dependencies.
- `README.md` — this file.

## Quick start (run locally)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python scripts/curate_metadata.py --input data/sample_metadata.csv --output data/curated_sample.csv
