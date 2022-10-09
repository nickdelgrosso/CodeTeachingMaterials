import argparse

from utils_jupyter import extract_requirements


parser = argparse.ArgumentParser(description='Collect Pypi requirements from the import lines of a notebook.')
parser.add_argument('notebooks', type=str, nargs='+', help='Notebook filenames')
args = parser.parse_args()
reqs = extract_requirements(*args.notebooks)
if reqs:
    print('\n'.join(reqs))
        
