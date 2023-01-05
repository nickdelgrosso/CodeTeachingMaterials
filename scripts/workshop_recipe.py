import yaml


def create_recipe(url, sessions) -> dict:    
    recipe = {
        'buildFolder': 'build/new',
        'status': 'running',
        'git': {
            'sync': True,
            'branch': 'main',
            'remoteName': 'origin',
            'remoteURL': url,
        },
        'readme': {
            'addDeepnoteShortcut': True,
            'addGitpodShortcut': True,
        },
        'sessions': sessions,
        'project': [
            'LICENSE',
            'jupyter_lab_config.py',
            '.gitpod.yml',
            '.gitignore',
        ]
    }
    return recipe


def create_session(title, unit_paths, unit_names):
    session = {
        'title': title,
        'include': True,
        'includeSolutions': False,
        'units':  [{'file': str(path), 'filename': f"Session{idx}/{name}"} for path, name in zip(unit_paths, unit_names)],
    }
    return session

def serialize_recipe(recipe) -> str:
    return yaml.dump(recipe, Dumper=yaml.CSafeDumper, sort_keys=False)


