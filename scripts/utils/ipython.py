

def in_interactive_mode(envs=["ZMQInteractiveShell", "TerminalInteractiveShell"]) -> bool:
    try:
        return get_ipython().__class__.__name__ in envs  # type: ignore
    except NameError:
        return False


def set_debugger_to_ipdb() -> None:
    import sys
    import ipdb
    sys.breakpointhook = ipdb.set_trace


