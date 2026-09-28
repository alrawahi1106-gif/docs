"""Append a value to a list and return the list."""


def list_accumulator(item, items=None):
    """Append item to items and return items.

    items defaults to a new empty list on each call. A literal [] default
    would be created once and shared across calls, so values would pile up.
    """
    if items is None:
        items = []
    items.append(item)
    return items


if __name__ == "__main__":
    print(list_accumulator(1))
    print(list_accumulator(2))

    existing = ["a"]
    print(list_accumulator("b", existing))
    print(existing)
