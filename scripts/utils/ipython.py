

def in_interactive_mode(envs=["ZMQInteractiveShell", "TerminalInteractiveShell"]) -> bool:
    try:
        return get_ipython().__class__.__name__ in envs
    except NameError:
        return False