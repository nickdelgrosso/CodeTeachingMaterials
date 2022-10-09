import argparse

import utils_jupyter

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# Get Requirements
def print_reqs(args):
    reqs = utils_jupyter.extract_requirements(*args.notebooks)
    if reqs:
        print('\n'.join(reqs))
parser_requirements = subparsers.add_parser('requirements')
parser_requirements.add_argument('notebooks', type=str, nargs='+', help='Notebook filenames')
parser_requirements.set_defaults(func=print_reqs)


# Studentize Notebooks
def studentize_notebooks(args):
    utils_jupyter.studentize_notebooks(*args.input, suffix=args.suffix, tag=args.tag)
parser_studentize = subparsers.add_parser('studentize')
parser_studentize.add_argument("input", type=str, nargs='+', help="Input notebooks")
parser_studentize.add_argument("--suffix", type=str, default="_student", help="Suffix for the output notebooks")
parser_studentize.add_argument("--tag", type=str, default="exercise", help="Tag to strip")
parser_studentize.set_defaults(func=studentize_notebooks)


if __name__ == '__main__':
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()
