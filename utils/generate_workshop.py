from __future__ import annotations

from pathlib import Path
from shutil import copy2
from subprocess import Popen

import yaml

import get_requirements
import git_sync


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
readme_path = basedir / "README.md"
readme_path.write_text(md_text)


# Create Requirements file
reqs  = set()
for notebook in list(basedir.glob('**/*.ipynb')):
    reqs.update(get_requirements.main(notebook))
requirements_path = basedir / "requirements.txt"
requirements_path.write_text('\n'.join(reqs))

# Clear out all the existing files, except for git
Popen(['rm', '-Rf', str(basedir / '!(git)')])  

# Files to simply copy over

for file in recipe['project']:
    copy2(file, basedir / Path(file).name)

print(f'Generated Workshop done: {str(basedir)}')

git_sync.sync_with_github(
    basedir=basedir,
    remote_url=recipe['git']['remote-url'],
    remote_name=recipe['git']['remote-name'],
    remote_branch=recipe['git']['remote-branch'],
)

print(f'Synced up with {git_sync.github_url_from_ssh_address(recipe["git"]["remote-url"])}')