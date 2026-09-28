"""Append a value to a list and return the list."""


def list_accumulator(item, items=[]):
    """Append item to items and return items.

    The default list is created once, when the function is defined, so calls
    that omit items all append to the same shared list.
    """
    items.append(item)
    return items


if __name__ == "__main__":
    print(list_accumulator(1))
    print(list_accumulator(2))
    print(list_accumulator(3))

    l = ["a"]
    print(list_accumulator("b", l))
    print(list_accumulator("c", l))
    print(list_accumulator(4))
