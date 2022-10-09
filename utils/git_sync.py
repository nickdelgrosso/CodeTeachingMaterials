
#%%
from pathlib import Path
from git import Repo, GitCommandError
from datetime import datetime


def sync_with_github(basedir: Path, remote_url, remote_name="origin", remote_branch="master") -> None:

    # Create repo, if not yet done.
    repo = Repo.init(basedir)
    git = repo.git  # use git commands directly
    try:
        git.remote("add", remote_name, remote_url)
    except GitCommandError: # it exists already, usually
        pass

    #%% git
    git.add("*")
    try:
        git.commit("-m", f"update {datetime.now().isoformat()}")
    except GitCommandError:  # nothing to commit
        pass

    git.pull(remote_name, remote_branch, '--rebase')
    git.push(remote_name, remote_branch)


def github_url_from_ssh_address(ssh: str) -> str:
    return ssh.replace("git@", "https://").replace(".git", "")




if __name__ == '__main__':
    sync_with_github(
        basedir=Path('build/intro2python'),
        remote_name="origin",
        remote_branch="master",
        remote_url="git@github.com:CodingForScientists/Intro2Python.git",

    )