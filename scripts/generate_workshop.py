from __future__ import annotations

from pathlib import Path
from shutil import copy2
from subprocess import Popen

import yaml

from utils.jupyter import extract_requirements, read_notebook, strip_cells, write_notebook
import sync_git

# Read the configuration file
recipe_filename = Path('workshops/intro2python.recipe.md')
*_, yaml_text, md_text = recipe_filename.read_text().split('---')
recipe = yaml.load(yaml_text, Loader=yaml.CSafeLoader)
basedir = Path(recipe['buildFolder'])

# Clear out all the existing files, except for git, and copy new files
Popen(['rm', '-Rf', str(basedir / '!(git)')])  
for file in recipe['project']:
    copy2(file, basedir / Path(file).name)

# Copy Notebooks
for session in recipe['sessions']:
    for unit in session['units']:
        orig_notebook_file = unit['file']
        orig_notebook = read_notebook(orig_notebook_file)
        new_notebook = orig_notebook
        # new_notebook = strip_cells(orig_notebook, tag='exercise')
        to_path = basedir / unit['filename']
        
        to_path.parent.mkdir(parents=True, exist_ok=True)
        write_notebook(to_path, new_notebook)

        # copy2(orig_notebook_file, to_path)


# Create Readme
(basedir / "README.md").write_text(md_text)

# Create Requirements fil
reqs = extract_requirements(*basedir.glob('**/*.ipynb'))
(basedir / "requirements.txt").write_text('\n'.join(reqs))

# Sync with git
# sync_git.sync_with_github(
#     basedir=basedir,
#     remote_url=recipe['git']['remote-url'],
#     remote_name=recipe['git']['remote-name'],
#     remote_branch=recipe['git']['remote-branch'],
# )

print(f'Generated Workshop done: {str(basedir)}')
print(f'Synced up with {sync_git.github_url_from_ssh_address(recipe["git"]["remote-url"])}')