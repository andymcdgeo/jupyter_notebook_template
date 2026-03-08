# Jupyter Notebook Cookiecutter Template

A cookiecutter template for geoscience Jupyter notebook projects that makes good habits automatic — sensible project structure, centralised path management, consistent plotting defaults, and data loading helpers, all ready to go from the first `cookiecutter` command.

> **Read the full article:**
> - [Part 1: The Project Structure That Makes Good Jupyter Notebook Habits Automatic](https://medium.com/p/5b396b9cadda)
> - Part 2: To be published

---

## Requirements

- Python 3.8+
- [cookiecutter](https://cookiecutter.readthedocs.io/) — install with pip or conda:

```bash
pip install cookiecutter
# or
conda install -c conda-forge cookiecutter
```

---

## Usage

Run cookiecutter and point it at this template:

```bash
cookiecutter c:/Projects/cookiecutter_templates/jupyter_notebook_template/
```

Or, if the template is hosted on GitHub:

```bash
cookiecutter gh:your-username/jupyter-notebook-template
```

You will be prompted for the following:

| Prompt | Default | Description |
|---|---|---|
| `project_name` | `My Geoscience Project` | Human-readable project name |
| `project_slug` | *(auto-derived)* | Directory name (spaces → underscores, lower-cased) |
| `author` | `Andy McDonald` | Your name |
| `description` | `A short description of the project` | One-line project summary |
| `python_version` | `3.11` | Python version for the project |
| `profile` | `full` | `full` for the complete setup, `quick` for a minimal setup |

---

## Profiles

### `full` (recommended)

The complete project scaffold:

```
my_project/
├── notebooks/
│   ├── 01_exploration.ipynb   # Scratch pad — imports & paths pre-filled
│   ├── 02_analysis.ipynb      # Clean analysis notebook
│   └── archive/               # Old notebook versions
├── src/
│   ├── config.py              # Central path management
│   ├── plotting.py            # rcParams defaults + save_fig()
│   └── data_loaders.py        # load_csv() and save_processed()
├── data/
│   ├── raw/
│   └── processed/
├── outputs/
│   └── figures/
├── requirements.txt
├── CHANGELOG.md
├── .gitignore
└── README.md
```

### `quick`

A minimal setup — notebooks and data folders only. Removes `src/`, `notebooks/archive/`, `02_analysis.ipynb`, `data/processed/`, `CHANGELOG.md`, and `.gitignore`.

---

## What you get

- **`src/config.py`** — `find_data()` locates the project root at runtime; `PROCESSED` and `FIGURES` path constants keep notebook paths consistent regardless of where a notebook is opened from.
- **`src/plotting.py`** — Applies sensible matplotlib `rcParams` defaults and provides a `save_fig()` helper that prefixes figures with today's date.
- **`src/data_loaders.py`** — `load_csv()` and `save_processed()` thin wrappers that use the central config paths.
- **Pre-filled notebooks** — `01_exploration.ipynb` opens with the standard imports and path setup already written.

---

## Further reading

- [Part 1: The Project Structure That Makes Good Jupyter Notebook Habits Automatic](https://medium.com/p/5b396b9cadda)
- Part 2: To be published
