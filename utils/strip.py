# %% Imports
from typing import List, Optional

from . import utils


# %% Main
def main(input_filename: str, output_filename: str, strip_tag: list[str] = []) -> None:
    """
    Strip cells from a notebook with the given tag.
    """
    notebook = utils.read_notebook(input_filename)
    new_cells = list(utils.strip_cells(notebook["cells"], strip_tag=strip_tag))
    new_notebook = utils.update_notebook_with_new_cells(notebook, new_cells)
    utils.write_notebook(new_notebook, output_filename)



# %% CLI
def cli(args: Optional[List[str]] = None) -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str, help="Input notebook")
    parser.add_argument("output", type=str, help="Output notebook")
    parser.add_argument("--strip-tag", type=str, default="exercise", help="Tag to strip")

    parsed_args = parser.parse_args(args)
    main(
        input_filename=parsed_args.input, 
        output_filename=parsed_args.output, 
        strip_tag=parsed_args.strip_tag,
    )

if __name__ == "__main__" and not __interactive:
    cli()

