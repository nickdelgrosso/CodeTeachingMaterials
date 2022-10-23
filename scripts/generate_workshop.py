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
import sync_git

import sys
import ipdb
sys.breakpointhook = ipdb.set_trace

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
    (basedir / "README.md").write_text(md_text)

    # # Copy Notebooks
    for session in recipe['sessions']:
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

    if recipe['git']:
        sync_git.sync_with_github(
            basedir=basedir,
            remote_url=recipe['git']['remoteURL'],
            remote_name=recipe['git']['remoteName'],
            remote_branch=recipe['git']['branch'],
        )

    # print(f'Generated Workshop done: {str(basedir)}')
    # print(f'Synced up with {sync_git.github_url_from_ssh_address(recipe["git"]["remote-url"])}')