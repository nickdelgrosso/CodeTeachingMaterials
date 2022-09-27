from argparse import ArgumentParser
from dataclasses import dataclass, field
import json
from pathlib import Path
from typing import Optional, TypedDict


class JupyterNotebook(TypedDict):
    cells: list['JupyterCell']


def read_notebook(filename: str) -> JupyterNotebook:
    return json.loads(Path(filename).read_text())


def write_notebook(notebook: JupyterNotebook, filename: str) -> None:
    Path(filename).write_text(json.dumps(notebook, indent=4))


class JupyterCell(TypedDict):
    cell_type: str
    source: list[str]


@dataclass
class ExerciseSection:
    start_idx: int
    end_idx: Optional[int] = None
    exclude: list[int] = field(default_factory=list)

    @classmethod
    def from_cells(cls, cells: list[JupyterCell]) -> list['ExerciseSection']:
        sections = []
        current: Optional[ExerciseSection] = None
        do_exclude = False
        for idx, cell in enumerate(cells):
            match cell, current, do_exclude:
                case {'cell_type': 'markdown', 'source': source}, None, _:
                    text = ''.join(source).replace('*', '').replace('#', '')
                    if 'exercise' in text.lower():
                        current = ExerciseSection(start_idx=idx)
                        do_exclude = False
                case {'cell_type': 'markdown', 'source': source}, ExerciseSection(), False:
                    text = ''.join(source)
                    if text.startswith('#'):
                        current.end_idx = idx
                        sections.append(current)
                        current = None
                    elif 'example' in text.lower():
                        do_exclude = True
                case {'cell_type': 'code'}, ExerciseSection(), True:
                    current.exclude.append(idx)
                case {'cell_type': 'markdown'}, ExerciseSection(), True:
                    do_exclude = False
                    
        return sections

    def preview(self, cells: list[JupyterCell]) -> str:
        lines = []
        for cell in cells[self.start_idx:self.end_idx]:
            match cell:
                case {'cell_type': 'markdown', 'source': source}:
                    lines.extend('M | ' + line.strip() for line in source)
                case {'cell_type': 'code', 'source': source}:
                    if source:
                        lines.extend('C | ' + line for line in source)
                    else:
                        lines.append('C | ')
        return '\n'.join(lines)
                    

def studentize(cells: list[JupyterCell], section: ExerciseSection) -> list[JupyterCell]:
    new_cells = cells.copy()
    for idx, cell in enumerate(new_cells):
        if section.start_idx <= idx < section.end_idx and idx not in section.exclude and cell['cell_type'] == 'code':
            cell['source'] = ''
            cell['outputs'] = ''
    return new_cells


def studentize_notebook(notebook: JupyterNotebook) -> JupyterNotebook:
    cells = notebook['cells']
    for section in ExerciseSection.from_cells(cells):
        cells = studentize(cells=cells, section=section)
    new_notebook = notebook | {'cells': cells}
    return new_notebook


def main():
    parser = ArgumentParser(description="Make a copy notebook of a notebook that has with the exercises sections blanked out, for students to fill out.")
    parser.add_argument('notebooks', nargs='+', help='Notebook files to copy')
    parser.add_argument('--suffix', default='_student', help='text for the end of the studentized noteook')
    args = parser.parse_args()


    for filename in args.notebooks:
        
        path = Path(filename)
        if path.stem.endswith(args.suffix):
            continue

        new_filename = path.with_stem(Path(filename).stem + args.suffix)
        write_notebook(
            notebook=studentize_notebook(notebook=read_notebook(filename=filename)), 
            filename=new_filename,
        )
        print(f'Created {new_filename}')


if __name__ == '__main__':
    main()