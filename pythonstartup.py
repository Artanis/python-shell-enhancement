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

    success = False
    try:
        readline.read_history_file(history_file)
        success = True
    except IOError:
        try:
            open(history_file, 'a').close()
            success = True
        except IOError as e:
            print("Failed to open history file {0}: {1}.".format(history_file, e.strerror))

    if success:
        atexit.register(readline.write_history_file, history_file)
        print('Persistent session history and tab completion are enabled.')
    else:
        print("Tab completion is enabled.")
