from __future__ import annotations

from pathlib import Path
from shutil import copy2
from subprocess import Popen

import yaml

from utils_jupyter import extract_requirements
import sync_git


workshop_md = Path('intro2python.recipe.md')
f = Path('workshops') / workshop_md
text = f.read_text()

*rst, yaml_text, md_text = text.split('---')
yaml_text = yaml_text.strip()

recipe = yaml.load(yaml_text, Loader=yaml.CSafeLoader)
basedir = Path('build') / workshop_md.stem.split('.')[0]

# Move Notebooks
files = {}
for session in recipe['sessions']:
    for unit in session['units']:
        from_path = Path(unit['file'])
        assert from_path.exists(), from_path
        to_path = basedir / session['foldername'] / unit['filename']
        to_path.parent.mkdir(parents=True, exist_ok=True)
        copy2(from_path, to_path)


# Create Readme
(basedir / "README.md").write_text(md_text)

# Create Requirements fil
reqs = extract_requirements(*basedir.glob('**/*.ipynb'))
(basedir / "requirements.txt").write_text('\n'.join(reqs))

# Clear out all the existing files, except for git, and copy new files
Popen(['rm', '-Rf', str(basedir / '!(git)')])  
for file in recipe['project']:
    copy2(file, basedir / Path(file).name)

print(f'Generated Workshop done: {str(basedir)}')

sync_git.sync_with_github(
    basedir=basedir,
    remote_url=recipe['git']['remote-url'],
    remote_name=recipe['git']['remote-name'],
    remote_branch=recipe['git']['remote-branch'],
)

print(f'Synced up with {sync_git.github_url_from_ssh_address(recipe["git"]["remote-url"])}')