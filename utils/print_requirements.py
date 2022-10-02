"""
Prints requirements from a given notebook.
"""

import argparse
from pathlib import Path
from typing import Dict

def main() -> None:
    parser = argparse.ArgumentParser(description='Collect Pypi requirements from the import lines of a notebook.')
    parser.add_argument('notebooks', type=str, nargs='+', help='Notebook filenames')  # Get notebook filename(s) as argument
    parser.add_argument('--output', type=str, default='requirements.txt', help='Output filename')
    parser.add_argument('--debug', action='store_true', help='Print debug info')
    args = parser.parse_args()
    run(filenames=args.notebooks, output=args.output if hasattr(args, 'output') else None)
    



def run(filenames: str, output: str = None, debug: bool = False) -> None:
    for filename in filenames:
        cells = _get_cells_from_notebook(filename)
        requirements = _get_requirements_from_cells(cells)
        pypi_requirements = [_get_pypi_name_from_package(package) for package in requirements]

        if debug:
            print('\n'.join(pypi_requirements))
        else:
            (Path(filename).parent / output).write_text('\n'.join(pypi_requirements))


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
        if cell['cell_type'] == 'code':
            source = [src] if isinstance((src := cell['source']), str) else src
            for line in source:
                if (kw := 'from') in line or (kw := 'import') in line:
                    words = line.split()
                    import_index = words.index(kw)
                    if import_index + 1 < len(words):
                        requirements.add(words[import_index + 1].split('.')[0])
                    else:
                        raise ValueError(f'Could not find import in line: {line}')
    return requirements


pypi_names = {
    'sklearn': 'scikit-learn',
    'skimage': 'scikit-image',
    'skvideo': 'scikit-video',
    'Bio': 'biopython',
    'cv2': 'opencv-python',
    'PIL': 'pillow',
    'torch': 'pytorch',
}


def _get_pypi_name_from_package(package) -> str:
    """Get pypi name from package."""    
    return pypi_names.get(package, package)




if __name__ == '__main__':
    main()
        