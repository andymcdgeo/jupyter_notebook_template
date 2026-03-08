# {{cookiecutter.project_name}}

**Author:** {{cookiecutter.author}}
**Description:** {{cookiecutter.description}}

---

## Project structure

```
{{cookiecutter.project_slug}}/
├── notebooks/
│   ├── 01_exploration.ipynb   # scratch pad
│   ├── 02_analysis.ipynb      # clean story
│   └── archive/               # old versions
├── src/
│   ├── config.py              # all paths
│   ├── data_loaders.py        # reusable loaders
│   └── plotting.py            # plot styling and saving
├── data/
│   ├── raw/                   # never modify these
│   └── processed/
├── outputs/
│   └── figures/
├── requirements.txt
└── CHANGELOG.md
```

## Setup

```bash
pip install -r requirements.txt
```

## Usage

Start with `notebooks/01_exploration.ipynb` for initial exploration.
Move clean, reproducible steps into `notebooks/02_analysis.ipynb`.

All paths are managed via `src/config.py` — no hardcoded file paths in notebooks.
