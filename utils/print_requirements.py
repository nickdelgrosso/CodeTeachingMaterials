"""
Prints requirements from a given notebook.
"""

import argparse
from pathlib import Path
from typing import Dict
import isort

def main() -> None:
    parser = argparse.ArgumentParser(description='Collect Pypi requirements from the import lines of a notebook.')
    parser.add_argument('notebooks', type=str, nargs='+', help='Notebook filenames')  # Get notebook filename(s) as argument
    parser.add_argument('--output', type=str, default='requirements.txt', help='Output filename')
    parser.add_argument('--debug', action='store_true', help='Print debug info')
    args = parser.parse_args()
    run(
        filenames=args.notebooks, 
        output=args.output if hasattr(args, 'output') else None,
        debug=args.debug,
    )
    



def run(filenames: str, output: str = None, debug: bool = False) -> None:
    for filename in filenames:
        cells = _get_cells_from_notebook(filename)
        requirements = _get_requirements_from_cells(cells)
        third_party_requirements = [package for package in requirements if isort.place_module(package) != 'STDLIB']
        pypi_requirements = [_get_pypi_name_from_package(package) for package in third_party_requirements]
        sorted_requirements = list(sorted(pypi_requirements))

        if debug:
            print('\n'.join(sorted_requirements))
        else:
            (Path(filename).parent / output).write_text('\n'.join(sorted_requirements))


def _get_cells_from_notebook(notebook) -> Dict:
    """Get cells from notebook."""
    import json
    with open(notebook) as f:
        nb = json.load(f)
    cells = nb['cells']
    return cells


def _get_requirements_from_cells(cells) -> set[str]:
    """Get requirements from cells."""
    requirements = set()
    for cell in cells:
        source = [src] if isinstance((src := cell['source']), str) else src
        if cell['cell_type'] == 'code':
            import_reqs = set(_reqs_from_imports(source))
            requirements = requirements.union(import_reqs)
        pip_reqs = set(_reqs_from_pip_install(source))
        requirements = requirements.union(pip_reqs)
        
    return requirements


def _reqs_from_pip_install(source: list[str]):
    r"""
    Examples:
    >>> list(_reqs_from_pip_install(["This is how to install a package\n", "`!pip install openpyxl`\n"]))
    ['openpyxl']

    """
    assert isinstance(source, list)
    for line in source:
        if 'pip install' in line:
            start = line.index('pip install')
            req = line[start:].split()[2]
            req = ''.join(c for c in req if c not in '`()!#')
            yield req


def _reqs_from_imports(source: list[str]):
    for line in source:
        if (kw := 'from') in line or (kw := 'import') in line:
            words = line.split()
            import_index = words.index(kw)
            if import_index + 1 < len(words):
                req = words[import_index + 1].split('.')[0]
                yield req
            else:
                raise ValueError(f'Could not find import in line: {line}')


pypi_names = {
    'sklearn': 'scikit-learn',
    'skimage': 'scikit-image',
    'skvideo': 'scikit-video',
    'Bio': 'biopython',
    'cv2': 'opencv-python',
    'PIL': 'pillow',
    'torch': 'pytorch',
    'pptx': 'python-pptx',
}


def _get_pypi_name_from_package(package) -> str:
    """Get pypi name from package."""    
    return pypi_names.get(package, package)




if __name__ == '__main__':
    main()
        