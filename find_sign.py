"""Find Unicode characters whose name contains "SIGN"."""

import unicodedata


def find_sign():
    """Return (code point, character, name) tuples for names containing "SIGN".

    Searches code points 0 through 2048 and skips any without a name.
    """
    results = []
    for code_point in range(2049):
        char = chr(code_point)
        name = unicodedata.name(char, None)
        if name is not None and "SIGN" in name:
            results.append((code_point, char, name))
    return results


if __name__ == "__main__":
    signs = find_sign()
    print(len(signs))
    for entry in signs[:5]:
        print(entry)
