#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as exc:
        sys.stderr.write("Exception: {}\n".format(exc))
        result = None

    return (result)

