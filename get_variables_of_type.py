"""Find global variables whose value is an instance of a given type."""

import sys


def get_variables_of_type(search_type):
    """Return the names of global variables whose value is an instance of search_type.

    The search runs over the global scope of the caller, so the function works
    both when called from this module and when imported into another one.
    """
    caller_globals = sys._getframe(1).f_globals
    return [
        name
        for name, value in list(caller_globals.items())
        if isinstance(value, search_type)
    ]


if __name__ == "__main__":
    count = 3
    ratio = 0.5
    label = "hello"
    other_label = "world"

    print(get_variables_of_type(str))
    print(get_variables_of_type(int))
    print(get_variables_of_type((int, float)))
