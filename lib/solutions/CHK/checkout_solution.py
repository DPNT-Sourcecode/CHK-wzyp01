

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str):
        return -1

    empty_string = skus\
        .replace("A", "")\
        .replace("B", "")\
        .replace("C", "")\
        .replace("D", "")\
        .replace("E", "")

    if len(empty_string) > 0:
        return -1

    As = skus.count("A")
    Bs = skus.count("B")
    Cs = skus.count("C")
    Ds = skus.count("D")
    Es = skus.count("E")

    price_A = 50
    price_B = 30
    price_C = 20
    price_D = 15
    price_E = 40

    five_As_price = 200
    three_As_price = 130
    two_Bs_price = 45

    temp_Es = Es
    while temp_Es >= 2:
        temp_Es -= 2
        if Bs > 0:
            Bs -= 1
            
    ret = 0

    while As >= 5:
        ret += five_As_price
        As -= 5

    while As >= 3:
        ret += three_As_price
        As -= 3

    while Bs >= 2:
        ret += two_Bs_price
        Bs -= 2

    ret += As*price_A
    ret += Bs*price_B
    ret += Cs*price_C
    ret += Ds*price_D
    ret += Es*price_E

    return ret


if __name__ == "__main__":
    print(checkout("AAA"))
    print(checkout("AABB"))
    print(checkout("EEBB"))
