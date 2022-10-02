import difflib
from pathlib import Path
from subprocess import Popen


def void(*args, **kwargs) -> None:
    """swallows all inputs."""
    return None



def verify(
    name: str, 
    data: str, 
    directory: str, 
    approve_diff: bool = False, 
    # has_interesting_diffs = lambda a, b: a != b,  # slow: = lambda a, b: bool(''.join(difflib.unified_diff(a, b))),
    has_interesting_diffs = lambda filename1, filename2: Path(filename1).read_text() != Path(filename2).read_text(),
    show_diffs = lambda f1, f2: print(''.join(difflib.unified_diff(f1, f2))),
    write = lambda filename, data: Path(filename).write_text(data),
    read = lambda filename: Path(filename).read_text(),
):
    """Mini Approval Testing tool."""

    # Create directory for saving test run to cache
    filesystem_safe_name = name.replace('/', '__')
    save_path = Path(directory) / Path(filesystem_safe_name).with_suffix('') / filesystem_safe_name
    save_path.parent.mkdir(parents=True, exist_ok=True)

    # Create filenames to reference for the "approved" (already-checked) and received (currently-being checked) files
    approved_filename = save_path.with_suffix('.approved' + save_path.suffix)
    received_filename = save_path.with_suffix('.received' + save_path.suffix)

    # Put data into the received file
    write(received_filename, data)

    # On first run: Just update the approved file with the current data.
    if not approved_filename.exists():
        write(approved_filename, data)
        return

    # On "approved changes" runs: just copy the received file to the approved file.
    received_data = read(received_filename)
    if approve_diff:
        write(approved_filename, received_data)
        return

    # On subsequent runs, do diff checking between the already-approved data and the new data.
    if has_interesting_diffs(approved_filename, received_filename):
        raise AssertionError(show_diffs(received_filename, approved_filename))
    

        

        