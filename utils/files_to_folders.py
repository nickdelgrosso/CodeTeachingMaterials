from argparse import ArgumentParser
import os
from pathlib import Path
from shutil import move

def main():
    parser = ArgumentParser(description="Batch move files to their own project folders.")
    parser.add_argument('notebooks', nargs='+', help='Notebook files to move')
    parser.add_argument('--no-readme', action='store_false', help='Do not create README.md')
    parser.add_argument('--to', default='.', help='Destination folder')
    parser.add_argument('--prepend', default='', help='Prepend to folder name')

    args = parser.parse_args()

    for notebook in args.notebooks:
        os.makedirs(args.to, exist_ok=True)

        path = Path(notebook)
        if not path.exists():
            raise FileNotFoundError(f'Notebook {notebook} does not exist')
        
        folder_name = Path(args.prepend + args.to) / path.stem
        os.makedirs(name=folder_name, exist_ok=True)
        
        move(src=notebook, dst=folder_name)
        new_path = Path(folder_name) / notebook
        assert os.path.exists(new_path)

        # Create Readme
        if args.no_readme:
            readme_path = Path(folder_name) / 'README.md'
            with open(readme_path, 'w') as f:
                f.write(f'# {folder_name}\n')
        
        print(f'Moved: {notebook} -> {new_path}')
        

if __name__ == '__main__':
    main()