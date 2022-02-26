
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

    # check valid input by removing all valid skus and checking if string is length 0
    empty_string = skus

    for sku in prices:
        empty_string = empty_string.replace(sku, "")

    if len(empty_string) > 0:
        return -1

    # fill the number of each sku into the dict
    sku_counts = dict()
    for sku in prices:
        sku_counts[sku] = skus.count(sku)

    # special logic for the promotions

    # buy one type get another type free
    temp_Es = sku_counts["E"]
    while temp_Es >= 2:
        temp_Es -= 2
        if sku_counts["B"] > 0:
            sku_counts["B"] -= 1

    ret = 0

    # multipack prices
    multi_pack_prices = dict()
    # dict of promotions
    # tuple of tuples, which have number of items, then price
    # need to have highest number first
    multi_pack_prices["A"]= ((5, 200), (3, 130))
    multi_pack_prices["B"] = ((2, 45),)
    multi_pack_prices["F"] = ((3, 2 * prices["F"]),)
    multi_pack_prices["H"] = ((10, 80), (5, 45))
    multi_pack_prices["K"] = ((2, 150),)
    multi_pack_prices["P"] = ((5, 200),)
    multi_pack_prices["Q"] = ((3, 80),)
    multi_pack_prices["U"] = ((4, 3*prices["U"]),)
    multi_pack_prices["V"] = ((3, 130), (2, 90))

    for sku in sku_counts:
        if sku in multi_pack_prices:
            for n, multi_pack_price in multi_pack_prices[sku]:
                while sku_counts[sku] >= n:
                    ret += multi_pack_price
                    sku_counts[sku] -= n


    # tally up the individual prices
    for sku in sku_counts:
        ret += sku_counts[sku] * prices[sku]

    return ret


if __name__ == "__main__":
    print(checkout("A"))
    print(checkout("AAA"))
    print(checkout("AABB"))
    print(checkout("EEBB"))
    print(checkout("AAAAA"))
