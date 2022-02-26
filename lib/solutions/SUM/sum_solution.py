# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):

    if not isinstance(x, int):
        raise TypeError("x must be an integer")

    if not isinstance(y, int):
        raise TypeError("y must be an integer")

    if x < 0 or x > 100:
        raise ValueError("Value x cannot be negative or greater than 100")
    if y < 0 or y > 100:
        raise ValueError("Value y cannot be negative or greater than 100")

    ret = x + y
    return ret



