
from __future__ import annotations

from pathlib import Path
import json
from typing import TypedDict, Optional, List

# Wrappers
def extract_requirements(*notebook_filenames: str) -> List[str]:
    all_reqs = set()
    for filename in notebook_filenames:
        notebook = read_notebook(filename)
        reqs = get_requirements(notebook)
        all_reqs.update(reqs)
    return list(sorted(all_reqs))


def studentize_notebooks(*filenames: str, suffix: str = "_student", tag: str = "exercise") -> None:
    for filename in filenames:    
        fname = Path(filename)
        notebook = read_notebook(fname)
        new_notebook = strip_cells(notebook, tag=tag)
        write_notebook(fname.with_stem(fname.stem + suffix), new_notebook)


# Functions
def read_notebook(filename: str) -> Notebook:
    return json.loads(Path(filename).read_text())


def strip_cells(notebook: Notebook, tag: str = "exercise") -> Notebook:
    return notebook | {"cells": [c | {'source': [], 'outputs': []} if tag in c['metadata'].get('tags', []) else c.copy() for c in notebook['cells']]}


def write_notebook(filename: str, notebook: Notebook) -> None:
    Path(filename).write_text(json.dumps(notebook, indent=2))


def get_requirements(notebook: Notebook) -> List[str]:
    """Get all the requirements from the `%pip install` lines in a notebook."""
    cells = notebook['cells']
    reqs = set()
    for cell in cells:
        source = [src] if isinstance((src := cell['source']), str) else src
        prefix = '%pip install '
        for line in source:
            code = line[:find(line, '#')].strip()  # Remove comments
            code = line[:find(line, ';')].strip()  # Remove semicolon
            if code.startswith(prefix):
                reqs.update(code[len(prefix):].split(' '))
    return list(sorted(reqs))


# Types
class Notebook(TypedDict):
    cells: list[Cell]
    metadata: dict
    nbformat: int
    nbformat_minor: int


class Cell(TypedDict):
    cell_type: str
    source: str | list[str]
    metadata: CellMetadata
    outputs: list[dict]


class CellMetadata(TypedDict):
    tags: list[str]


# Utils
def find(s: str, sub: str) -> Optional[int]:
    """Find the index of the first occurrence of a substring string."""
    idx = s.find(sub)
    return idx if idx != -1 else None
