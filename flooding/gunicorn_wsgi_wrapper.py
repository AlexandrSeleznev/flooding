# The only reason for the existence of this function is that
# gunicorn's run() doesn't take argument, and the console scripts
# generated by Buildout do.

from gunicorn.app import wsgiapp


def run(argv=None):
    # Call gunicorn's run()
    wsgiapp.run()
