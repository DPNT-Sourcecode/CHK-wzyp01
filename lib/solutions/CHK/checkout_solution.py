

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    empty_string = skus.replace("A", "").replace("B", "").replace("C", "").replace("D", "")
    if len(empty_string) > 0:
        raise ValueError("Non valid characters in SKU")

    As = skus.count("A")
    Bs = skus.count("B")
    Cs = skus.count("C")
    Ds = skus.count("D")
    print(As)


if __name__ == "__main__":
    checkout("AAA")
    checkout("a")


