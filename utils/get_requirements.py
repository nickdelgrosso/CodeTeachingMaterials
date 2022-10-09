"""
Prints requirements from a given notebook.
"""

import argparse
from pathlib import Path
from typing import Dict, Iterator, Iterable, List
import isort

import utils

def cli() -> None:
    parser = argparse.ArgumentParser(description='Collect Pypi requirements from the import lines of a notebook.')
    parser.add_argument('notebooks', type=str, nargs='+', help='Notebook filenames')
    args = parser.parse_args()
    for filename in args.notebooks:
        reqs = main(filename=filename)
        if reqs:
            print('\n'.join(requirements))

    

def main(filename: str) -> List[str]:
    notebook = utils.read_notebook(filename)
    cells = notebook['cells']
    requirements = list(sorted(_get_requirements_from_cells(cells)))
    return requirements
    


def _get_requirements_from_cells(cells) -> Iterator[str]:
    """Get requirements from cells."""
    for cell in cells:
        source = [src] if isinstance((src := cell['source']), str) else src
        if cell['cell_type'] == 'code':
            yield from _get_requirements_from_source(source)


def _get_requirements_from_source(source: str | List[str]) -> Iterator[str]:
    r"""
    Examples:
    >>> list(_reqs_from_pip_install(["x = 3 + 2\n", "`!pip install openpyxl`\n"]))
    ['openpyxl']

    """
    assert isinstance(source, list)
    prefix = '!pip install'
    for line in source:
        if '#' in line:
            line = line[:line.index('#')].strip()
        if not line.startswith(prefix):
            continue
        line = line.replace(prefix, '').strip()
        reqs = line.split(' ')
        yield from iter(reqs)



if __name__ == '__main__':
    cli()
        