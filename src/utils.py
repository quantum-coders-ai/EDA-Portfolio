from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def set_mpl_defaults():
    plt.rcParams.update({
        "figure.figsize": (8, 5),
        "axes.grid": True,
        "axes.titlesize": 14,
        "axes.labelsize": 12
    })

def load_csv(path, **kwargs):
    path = Path(path)
    return pd.read_csv(path, **kwargs)

def save_fig(fig, out_path):
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, bbox_inches="tight", dpi=150)
