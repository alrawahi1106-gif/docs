"""Read a range of bytes from a file object."""


def read_at(f, offset, length):
    """Return length bytes read from f starting at offset.

    Fewer bytes come back if the range runs past the end of the file.
    """
    f.seek(offset)
    return f.read(length)


if __name__ == "__main__":
    import io

    f = io.BytesIO(b"0123456789")
    print(read_at(f, 2, 3))
    print(read_at(f, 0, 4))
    print(read_at(f, 8, 5))
