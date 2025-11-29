# Predoc Coding Sample – Jomana Abdelrahman

This repository contains a self-contained coding sample that demonstrates my ability to:

- Work with panel data
- Generate and clean datasets programmatically
- Implement causal inference techniques (difference-in-differences)
- Use Python, pandas, and statsmodels for empirical analysis
- Write clear, documented, and reproducible code
- Use SQL to query and summarize data

The project simulates a simple policy evaluation setting: a subset of units (e.g., firms or regions) are exposed to a policy at a given time, and we estimate the average treatment effect using a difference-in-differences framework.

## Repository structure

```text
.
├─ README.md
├─ requirements.txt
├─ data/
│   ├─ raw/
│   └─ processed/
├─ src/
│   ├─ generate_data.py
│   ├─ analysis_diff_in_diff.py
│   └─ utils.py
├─ notebooks/
│   └─ 01_exploratory_analysis.ipynb   # optional
└─ sql/
    └─ sample_queries.sql
```

## How to run

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Generate the synthetic panel dataset:

```bash
python src/generate_data.py
```
This will create `data/processed/sim_panel.csv`.

4. Run the difference-in-differences analysis:

```bash
python src/analysis_diff_in_diff.py
```
This will print summary tables to the console and save results (e.g., regression output) to `data/processed/` as needed.

---

## Technologies used

- Python 3.10+
- pandas
- numpy
- statsmodels
- matplotlib 
- SQL (sample queries in `sql/sample_queries.sql`)

--- 

## Notes

This repo is intended as an illustrative coding sample for pre-doctoral and research assistant applications. It mirrors the kinds of tasks common in applied microeconomics and empirical social science research: data generation and cleaning, merging, panel structure, and causal estimation.
