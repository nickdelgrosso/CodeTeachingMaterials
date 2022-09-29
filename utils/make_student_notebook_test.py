import difflib
from pathlib import Path
from utils import make_student_notebook
from glob import glob
from .verify_notebooks import verify
import pytest

notebook_files = glob('topics/**/*.ipynb')
notebook_files = [filename for filename in notebook_files if '_student' not in filename]


@pytest.mark.parametrize('filename', notebook_files[::5])
def test_studentize_doesnt_modify_original_files(filename):
    notebook_before_run = Path(filename).read_text()
    make_student_notebook.main(args=(filename,))
    notebook_after_run = Path(filename).read_text()
    assert not ''.join(difflib.unified_diff(notebook_before_run, notebook_after_run))



@pytest.mark.parametrize('filename', notebook_files[::5])
def test_same_result(request, filename):
    make_student_notebook.main(args=(filename, '--suffix', '_student'))
    new_filename = Path(filename).with_stem(Path(filename).stem + '_student')
    verify(
        name=new_filename.name, 
        data=new_filename.read_text(), 
        directory='./cached' + f'/{request.node.originalname}', 
        approve_diff=request.config.option.approve,
    )
    