# Configuration file for lab.

c = get_config()  # noqa

c.LabApp.collaborative = True
c.ServerApp.allow_origin = '*'
c.ServerApp.token = ''  # Yes, I understand it's insecure.  We'll see how it goes.
