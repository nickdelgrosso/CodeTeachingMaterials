
#%% Imports
from __future__ import annotations

import json
from typing import Iterator, TypedDict, List, Iterable


#%% utils
def in_interactive_mode(envs=["ZMQInteractiveShell", "TerminalInteractiveShell"]) -> bool:
    try:
        current_env = get_ipython().__class__.__name__
        if current_env in envs:
            return True
        else:
            return False
    except NameError:
        return False

__interactive = in_interactive_mode()


#%% Domain Types

class Notebook(TypedDict):
    cells: list[Cell]
    metadata: dict
    nbformat: int
    nbformat_minor: int

class Cell(TypedDict):
    cell_type: str
    source: str | list[str]
    metadata: dict
    outputs: list[dict]



#%% Load data
def read_notebook(filename: str) -> Notebook:
    with open(filename) as f:
        data = json.load(f)
    return data


if __interactive:
    data = read_notebook("F2.ipynb")

    data.keys()
    cells = data["cells"]
    print(len(cells))
    print(data.keys())
    print(data['metadata'])

#%% Empty out cells with tag "exercise"

def get_tags(cell: Cell) -> List[str]:
    """
    Returns the tags from a jupyter cell dict.

    Examples:
    
    Cell with two tags:
    >>> get_tags({'metadata': {'tags': ['exercise', 'solution']}})
    ['exercise', 'solution']

    Cell with empty list of tags:
    >>> get_tags({'metadata': {'tags': []}})
    []

    Cell with no tags key:
    >>> get_tags({'metadata': {}})
    []


    Not a valid cell:
    >>> get_tags({})
    Traceback (most recent call last):
    ...
    KeyError: 'metadata'
    """
    metadata = cell["metadata"]
    tags = metadata.get("tags", [])

    return tags

def strip_cells(cells: Iterable[Cell], strip_tag: str = "exercise") -> Iterator[Cell]:
    """
    Yield cells that have the given tag with their source and outputs removed.

    Examples:
    >>> cells = [
    ...     {'cell_type': 'code', 'source': 'print("hello")', 'outputs': [{'output_type': 'stream', 'text': 'hello'}], 'metadata': {'tags': ['exercise']}},
    ...     {'cell_type': 'code', 'source': 'print("world")', 'outputs': [{'output_type': 'stream', 'text': 'world'}], 'metadata': {}},
    ... ]
    >>> list(strip_cells(cells, strip_tag="exercise"))
    [{'cell_type': 'code', 'source': [], 'outputs': [], 'metadata': {'tags': ['exercise']}}, {'cell_type': 'code', 'source': 'print("world")', 'outputs': [{'output_type': 'stream', 'text': 'world'}], 'metadata': {}}]

    """
    for cell in cells:
        if strip_tag in get_tags(cell):
            yield cell | {'source': [], 'outputs': []}
        else:
            yield cell.copy()


if __interactive:
    new_cells = list(strip_cells(cells, strip_tag="exercise"))
    print(len([cell for cell in new_cells if "exercise" in get_tags(cell)]))


# %% Updated and Save Notebook
def update_notebook_with_new_cells(notebook: Notebook, new_cells: List[Cell]) -> Notebook:
    return notebook | {'cells': new_cells}


def write_notebook(notebook: Notebook, filename: str) -> None:
    with open(filename, "w") as f:
        json.dump(notebook, f)

if __interactive:
    new_notebook = update_notebook_with_new_cells(data, new_cells)
    write_notebook(new_notebook, "F2_stripped.ipynb")

