import datetime

import matplotlib.pyplot as plt

from config import FIGURES

plt.rcParams.update({
    'figure.figsize': (10, 6),
    'axes.spines.top': False,
    'axes.spines.right': False,
    'font.family': 'Arial',
    'axes.titlesize': 14,
    'axes.labelsize': 12,
})


def save_fig(fig, name: str, dpi: int = 150):
    """Save a figure to the outputs/figures directory with a date prefix."""
    date = datetime.date.today().strftime("%Y%m%d")
    filepath = FIGURES / f"{date}_{name}.png"
    fig.savefig(filepath, dpi=dpi, bbox_inches='tight')
    print(f"Saved: {filepath}")
