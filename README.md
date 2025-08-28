# EDA Portfolio

A 2-week, 2–3 dataset Exploratory Data Analysis (EDA) portfolio.

## 📊 Datasets (choose 2–3)
- Airbnb NYC — rental prices, location trends
- Netflix Movies & TV Shows — genres, years, ratings
- Ride-hailing trips (e.g., NYC TLC trips as proxy for Uber/Lyft) — demand vs time of day

> Replace or add datasets as you like.

## 🧰 Tools
Python • Jupyter • NumPy • Pandas • Matplotlib • Seaborn • Plotly

## 📅 Plan (Sept 1–14, 2025)
- Week 1: loading, cleaning, basic EDA
- Week 2: advanced viz, insights, polish + README

## ✅ Deliverables
- 1 notebook per dataset in `notebooks/`
- Cleaned data (optional) in `data/processed/`
- Plots saved to `reports/figures/`
- README updated with dataset links, approach, and key insights

## 🔧 How to run
```bash
# (Option A) Using venv
python -m venv .venv
./.venv/Scripts/activate  # Windows
pip install -r requirements.txt
jupyter notebook

# (Option B) Using conda
conda env create -f environment.yml
conda activate eda-portfolio
jupyter notebook
```

## 🗂️ Repo Structure
```
eda-portfolio/
├─ data/
│  ├─ raw/          # put original CSV/JSON here (unmodified)
│  ├─ interim/      # intermediate outputs
│  └─ processed/    # cleaned datasets saved here
├─ notebooks/
│  ├─ 01_airbnb_nyc.ipynb
│  ├─ 02_netflix_titles.ipynb
│  └─ 03_trips_timeseries.ipynb
├─ reports/
│  └─ figures/      # charts exported from notebooks
├─ src/
│  ├─ __init__.py
│  └─ utils.py      # helpers for loading/cleaning/plot style
├─ requirements.txt
├─ environment.yml
└─ README.md
```

---

*Generated on 2025-08-28.*
