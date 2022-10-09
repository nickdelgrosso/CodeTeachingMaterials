from pathlib import Path
from datetime import datetime
from subprocess import run


def sync_with_github(basedir: Path, remote_url, remote_name="origin", remote_branch="master") -> None:
    cmds = f"""
    cd {str(basedir)};
    git init;
    git add *;
    git commit -m "update {datetime.now().isoformat()}";
    git remote add {remote_name} {remote_url} 2> /dev/null;
    git pull origin {remote_branch};
    git push origin {remote_branch};
    """
    run(cmds, shell=True)


def github_url_from_ssh_address(ssh: str) -> str:
    return ssh.replace(':', '/').replace("git@", "https://").replace(".git", "")




if __name__ == '__main__':
    sync_with_github(
        basedir=Path('build/intro2python'),
        remote_name="origin",
        remote_branch="master",
        remote_url="git@github.com:CodingForScientists/Intro2Python.git",

    )