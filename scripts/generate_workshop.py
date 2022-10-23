from __future__ import annotations
from genericpath import isfile
import os

from pathlib import Path
from shutil import copy2
import shutil
from subprocess import Popen
import logging

import yaml

from utils.jupyter import extract_requirements, read_notebook, strip_cells, write_notebook
from utils.ipython import set_debugger_to_ipdb
from utils.markdown import get_gitpod_markdown_shortcut, get_deepnote_markdown_shortcut
import sync_git

set_debugger_to_ipdb()
# logging.basicConfig(level=logging.DEBUG)

# Read the configuration file

def clear_directory(basedir, excludes = ['.git']):
    for name in basedir.rglob('*'):
        if any(exclude in str(name) for exclude in excludes):
            continue
        if name.is_file():
            Popen(['rm', str(name)]) 
            logging.log(logging.DEBUG, f'removed {str(name)}')
        elif name.is_dir():
            Popen(['rm', '-Rf', str(name)])  
            logging.log(logging.DEBUG, f'removed {str(name)}')


# Script

recipe_filenames = Path('workshops').glob('*.recipe.md')

for recipe_filename in recipe_filenames:
    *_, yaml_text, md_text = recipe_filename.read_text().split('---')
    
    
    recipe = yaml.load(yaml_text, Loader=yaml.CSafeLoader)
    if recipe['status'] in ['finished']:
        logging.log(logging.DEBUG, f'skipping {str(recipe_filename)}')
        continue  
    else:
        logging.log(logging.DEBUG, f'building {str(recipe_filename)}')
    
    basedir = Path(recipe['buildFolder'])
    basedir.mkdir(parents=True, exist_ok=True)
    
    clear_directory(basedir, excludes=['/.git'])

    for file in recipe['project']:
        copy2(file, basedir / Path(file).name)
    
    # Create Readme
    print('readme-ing')
    shortcuts = ''
    if recipe.get('git').get('remoteURL') and recipe.get('readme').get('addDeepnoteShortcut'):
        logging.log(logging.DEBUG, 'adding Deepnote Link')
        shortcuts += get_deepnote_markdown_shortcut(recipe['git']['remoteName']) + '\n'
    if recipe.get('git').get('remoteURL') and recipe.get('readme').get('addGitpodShortcut'):
        logging.log(logging.DEBUG, 'adding Gitpod shortcut')
        shortcuts += get_gitpod_markdown_shortcut(recipe['git']['remoteName']) + '\n'
    md_text = shortcuts + md_text

    (basedir / "README.md").write_text(md_text)


    # # Copy Notebooks
    for session in recipe['sessions']:
        if not session.get('include'):
            continue
        for unit in session['units']:
            orig_notebook_file = unit['file']
            orig_notebook = read_notebook(orig_notebook_file)

            filename = (basedir / unit['filename'])
            filename.parent.mkdir(parents=True, exist_ok=True)
            if session.get('includeSolutions'):
                write_notebook(
                    filename.with_suffix('.solutions.ipynb'), 
                    orig_notebook
                )
            
            exercise_notebook = strip_cells(orig_notebook, tag='exercise')
            write_notebook(
                filename.with_suffix('.exercise.ipynb'), 
                exercise_notebook
            )


    # # Create Requirements file
    reqs = extract_requirements(*basedir.glob('**/*.ipynb'))
    (basedir / "requirements.txt").write_text('\n'.join(reqs))

    if recipe.get('git') and recipe['git'].get('sync'):
        sync_git.sync_with_github(
            basedir=basedir,
            remote_url=recipe['git']['remoteURL'],
            remote_name=recipe['git']['remoteName'],
            remote_branch=recipe['git']['branch'],
        )

    # print(f'Generated Workshop done: {str(basedir)}')
    # print(f'Synced up with {sync_git.github_url_from_ssh_address(recipe["git"]["remote-url"])}')