from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
LOCAL_RAW    = PROJECT_ROOT / "data" / "raw"
PROCESSED    = PROJECT_ROOT / "data" / "processed"
FIGURES      = PROJECT_ROOT / "outputs" / "figures"
CENTRAL_DATA = Path.home() / "geoscience_data"


def find_data(filename: str) -> Path:
    """Locate a data file in the local project or central shared data directory."""
    local = LOCAL_RAW / filename
    if local.exists():
        return local
    central = CENTRAL_DATA / filename
    if central.exists():
        return central
    raise FileNotFoundError(
        f"{filename} not found in:\n  {LOCAL_RAW}\n  {CENTRAL_DATA}"
    )
