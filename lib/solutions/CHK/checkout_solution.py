import numpy as np

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
          "K": 70,
          "L": 90,
          "M": 15,
          "N": 40,
          "O": 10,
          "P": 50,
          "Q": 30,
          "R": 50,
          "S": 20,
          "T": 20,
          "U": 40,
          "V": 50,
          "W": 20,
          "X": 17,
          "Y": 20,
          "Z": 21}
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
    cross_promotion_deals = dict()
    # tuple containing the item you get off, number of this item you need, and number of those that are free
    cross_promotion_deals["E"] = ("B", 2, 1)
    cross_promotion_deals["N"] = ("M", 3, 1)
    cross_promotion_deals["R"] = ("Q", 3, 1)

    for sku in cross_promotion_deals:
        (other_item_sku, n_needed, n_free) = cross_promotion_deals[sku]
        temp_this_sku = sku_counts[sku]
        while temp_this_sku >= n_needed:
            temp_this_sku -= n_needed
            if sku_counts[other_item_sku] > 0:
                sku_counts[other_item_sku] -= n_free
            if sku_counts[other_item_sku] < 0:
                sku_counts[other_item_sku] = 0

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
    multi_pack_prices["K"] = ((2, 120),)
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

    # first get counts and prices of the combo items
    # then sort them in descending order according to price
    combo_deal_skus = ["S", "T", "X", "Y", "Z"]
    count_sku_combo = []
    price_sku_combo = []

    for sku in combo_deal_skus:
        count_sku_combo.append(sku_counts[sku])
        price_sku_combo.append(prices[sku])

    combo_deal_skus = np.array(combo_deal_skus)
    count_sku_combo = np.array(count_sku_combo)
    price_sku_combo = np.array(price_sku_combo)

    indices = np.argsort(price_sku_combo)[::-1]
    combo_deal_skus = combo_deal_skus[indices]
    count_sku_combo = count_sku_combo[indices]
    price_sku_combo = price_sku_combo[indices]

    # if there are more than 3 of the combo items, remove them (starting with most expensive) and add 45 to price
    # need to keep checking that there are 3 or more combo items
    if sum(count_sku_combo) >= 3:
        # count_this_group tracks the trios
        count_this_group = 0
        # iterate through combo items
        for i in range(len(count_sku_combo)):
            # while there is at least one of this item, remove it from the counts
            while count_sku_combo[i] > 0:
                count_sku_combo[i] -= 1
                sku_counts[combo_deal_skus[i]] -= 1
                count_this_group += 1
                if count_this_group == 3:
                    count_this_group = 0
                    ret += 45
                    if np.sum(count_sku_combo) < 3:
                        break

    # tally up the individual prices
    for sku in sku_counts:
        ret += sku_counts[sku] * prices[sku]

    return ret


if __name__ == "__main__":
    print(checkout("ZZZS"))
    print(checkout("A"))
    print(checkout("AAA"))
    print(checkout("AABB"))
    print(checkout("EEBB"))
    print(checkout("AAAAA"))
    print(checkout("SSTTXX"))

