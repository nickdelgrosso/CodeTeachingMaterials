
def get_deepnote_markdown_shortcut(github_url: str) -> str:
    return f"[![Open in Deepnote](https://deepnote.com/buttons/launch-in-deepnote-small.svg)](https://www.deepnote.com/launch?template=data-science&url={github_url})"

def get_gitpod_markdown_shortcut(github_url: str) -> str:
    return f"[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#{github_url})"
