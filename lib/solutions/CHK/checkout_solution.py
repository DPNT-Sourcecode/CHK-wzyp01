
prices = {"A": 50,
          "B": 30,
          "C": 20,
          "D": 15,
          "E": 40,
          "F": 10,
          "G": 20,
          "H": 10,
          "I": 35,
          "J": 60,
          "K": 80,
          "L": 90,
          "M": 15,
          "N": 40,
          "O": 10,
          "P": 50,
          "Q": 30,
          "R": 50,
          "S": 30,
          "T": 20,
          "U": 40,
          "V": 50,
          "W": 20,
          "X": 90,
          "Y": 10,
          "Z": 50}
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str):
        return -1

    empty_string = skus

    for sku in prices:
        empty_string = empty_string.replace(sku, "")

    if len(empty_string) > 0:
        return -1

    sku_counts = dict()

    for sku in prices:
        sku_counts[sku] = skus.count(sku)

    five_As_price = 200
    three_As_price = 130
    two_Bs_price = 45
    three_Fs_price = 2*prices["F"]

    temp_Es = sku_counts["E"]
    while temp_Es >= 2:
        temp_Es -= 2
        if sku_counts["B"] > 0:
            sku_counts["B"] -= 1

    ret = 0

    while sku_counts["A"] >= 5:
        ret += five_As_price
        sku_counts["A"] -= 5

    while sku_counts["A"] >= 3:
        ret += three_As_price
        sku_counts["A"] -= 3

    while sku_counts["B"] >= 2:
        ret += two_Bs_price
        sku_counts["B"] -= 2

    while sku_counts["F"] >= 3:
        ret += three_Fs_price
        sku_counts["F"] -= 3

    for sku in sku_counts:
        ret += sku_counts[sku] * prices[sku]

    return ret


if __name__ == "__main__":
    print(checkout("A"))
    print(checkout("AAA"))
    print(checkout("AABB"))
    print(checkout("EEBB"))
    print(checkout("AAAAA"))

