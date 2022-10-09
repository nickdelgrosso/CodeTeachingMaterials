import argparse

from utils_jupyter import studentize_notebooks


parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, nargs='+', help="Input notebooks")
parser.add_argument("--suffix", type=str, default="_student", help="Suffix for the output notebooks")
parser.add_argument("--tag", type=str, default="exercise", help="Tag to strip")
args = parser.parse_args()

studentize_notebooks(*args.input, suffix=args.suffix, tag=args.tag)


