import os
import shutil

profile = "{{cookiecutter.profile}}"

FULL_ONLY = [
    "src",
    "notebooks/archive",
    "notebooks/02_analysis.ipynb",
    "data/processed",
    "CHANGELOG.md",
    ".gitignore",
]


def remove(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    elif os.path.isfile(path):
        os.remove(path)


if profile == "quick":
    for item in FULL_ONLY:
        remove(item)
    print("\nQuick project ready. Start with notebooks/01_exploration.ipynb")
else:
    print("\nFull project ready.")
    print("Explore: notebooks/01_exploration.ipynb")
    print("Analyse: notebooks/02_analysis.ipynb")
