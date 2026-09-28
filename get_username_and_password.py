"""Read a username and password from standard input."""

import sys


def get_username_and_password():
    """Return a (username, password) tuple read from sys.stdin.

    The username is the first line and the password is the second. getpass
    needs an interactive terminal, so both lines come from sys.stdin. Only the
    line ending is stripped, so spaces inside the password are kept.
    """
    username = sys.stdin.readline().rstrip("\r\n")
    password = sys.stdin.readline().rstrip("\r\n")
    return username, password


if __name__ == "__main__":
    print(get_username_and_password())
