from solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        for sku in checkout_solution.prices:
            assert checkout_solution.checkout(sku) == checkout_solution.prices[sku]

        assert checkout_solution.checkout("abc") == -1

        assert checkout_solution.checkout(1) == -1

        assert checkout_solution.checkout("A") == 50

        assert checkout_solution.checkout("B") == 30

        assert checkout_solution.checkout("C") == 20

        assert checkout_solution.checkout("D") == 15

        assert checkout_solution.checkout("F") == 10

        assert checkout_solution.checkout("FF") == 20

        assert checkout_solution.checkout("FFF") == 20

        assert checkout_solution.checkout("FFFF") == 30

        assert checkout_solution.checkout("FFFFF") == 40

        assert checkout_solution.checkout("FFFFFF") == 40

        assert checkout_solution.checkout("AAA") == 130

        assert checkout_solution.checkout("BB") == 45

        assert checkout_solution.checkout("AAAAA") == 200

        assert checkout_solution.checkout("AAAAAA") == 250

        assert checkout_solution.checkout("BBBB") == 90

        assert checkout_solution.checkout("AAAA") == 180

        assert checkout_solution.checkout("ABCD") == 115

        assert checkout_solution.checkout("BBEE") == 110

        assert checkout_solution.checkout("E") == 40

        assert checkout_solution.checkout("EB") == 70

        assert checkout_solution.checkout("BEE") == 80


        # check multibuys (post f)
        assert checkout_solution.checkout("HHHHHHHHHH") == 80
        assert checkout_solution.checkout("HHHHH") == 45

        assert checkout_solution.checkout("KK") == 150

        assert checkout_solution.checkout("PPPPP") == 200

        assert checkout_solution.checkout("QQQ") == 80

        assert checkout_solution.checkout("UUUU") == 3*checkout_solution.prices["U"]

        assert checkout_solution.checkout("VVV") == 130

        assert checkout_solution.checkout("VV") == 90



