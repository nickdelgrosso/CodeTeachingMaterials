from pathlib import Path

def get_notebook_paths() -> list[Path]:
    return list(Path('notebooks').glob('*.ipynb'))
