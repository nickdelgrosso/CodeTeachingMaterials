
import contextlib
import difflib
import json
from pathlib import Path
from utils import make_student_notebook
from glob import glob
import nbdime

import pytest

notebook_files = glob('topics/**/*.ipynb')
notebook_files = [filename for filename in notebook_files if '_student' not in filename]

@pytest.mark.skip
@pytest.mark.parametrize('filename', notebook_files[::5])
def test_studentize_doesnt_modify_original_files(filename):
    notebook_before_run = Path(filename).read_text()
    make_student_notebook.main(args=(filename,))
    notebook_after_run = Path(filename).read_text()
    assert not ''.join(difflib.unified_diff(notebook_before_run, notebook_after_run))



def verify(name: str, data: str, path: str, approve_diff: bool = False):
    filename = Path(path) / name
    filename.parent.mkdir(parents=True, exist_ok=True)
    if filename.exists():
        approved = filename.read_text().splitlines()
        received = data.splitlines()
        diff = ''.join(difflib.unified_diff(approved, received))
        if not diff:
            return
        elif diff and approve_diff:
            filename.write_text(data)
        else:
            raise AssertionError(diff)
    else:
        filename.write_text(data)


@pytest.mark.parametrize('filename', notebook_files[::5])
def test_same_result(request, filename):
    make_student_notebook.main(args=(filename, '--suffix', '_student'))
    orig_filename = Path(filename)
    new_filename = orig_filename.with_stem(orig_filename.stem + '_student')
    new_notebook = new_filename.read_text()
    verify(
        name=request.node.name.replace('/', '__') + new_filename.suffix, 
        data=new_notebook, 
        path='./cached', 
        approve_diff=request.config.option.approve,
    )
    
    