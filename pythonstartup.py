# Pulled these two examples together for the following code
# http://docs.python.org/2/library/rlcompleter.html#module-rlcompleter
# http://geoffford.wordpress.com/2009/01/20/python-repl-enhancement/


try:
    import readline
    import rlcompleter
    import atexit
    import os
    import sys
    import platform
except ImportError as exception:
    print('Shell Enhancement module problem: {0}').format(exception)
else:
    # Enable Tab Completion
    if sys.platform == 'darwin':     # different bind for OSX
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")

    # Enable History File
    history_file = os.environ.get("PYTHON_HISTORY_FILE", 
                                  os.path.join(os.environ['HOME'], 
                                               '.pythonhistory'))


    try:
        readline.read_history_file(history_file)
    except IOError as e:
        if e.errno != 2:
            # [Errno 2] happens when the file doesn't exist yet, and is normal.
            print("Could not open history file ({0}) for reading: {1}".format(
                history_file, e))

    def write_history_file(history_file):
        """Wrap readline.write_history_file and add error handling.

        """
        try:
            readline.write_history_file(history_file)
        except IOError as e:
            print("Could not open history file ({0}) for writing: {1}".format(
                history_file, e))

    atexit.register(write_history_file, history_file)

    print('Persistent session history and tab completion are enabled.')
