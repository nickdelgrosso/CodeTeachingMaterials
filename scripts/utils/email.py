def to_mailbox(email: str, first_name: str = "", last_name: str = "", ) -> str:
    """
    Convert name and email info to mailbox string format
    
    https://superuser.com/questions/1625686/what-is-the-email-address-format-name-email-called
    
    Example:
    >>> to_mailbox("Nick", "DG", "dg@google.com")
    'Nick DG <dg@google.com>'
    """
    return f"{first_name} {last_name} <{email}>".replace('  ', ' ').strip()

