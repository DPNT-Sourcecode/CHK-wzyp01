from solutions.CHK import checkout_solution
import pytest

class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("abc") == -1

        assert checkout_solution.checkout(1) == -1

        assert checkout_solution.checkout("A") == 50

        assert checkout_solution.checkout("B") == 30

        assert checkout_solution.checkout("C") == 20

        assert checkout_solution.checkout("D") == 15

        assert checkout_solution.checkout("AAA") == 130

        assert checkout_solution.checkout("BB") == 45

        assert checkout_solution.checkout("AAAAAA") == 260

        assert checkout_solution.checkout("BBBB") == 90

        assert checkout_solution.checkout("AAAA") == 180

        assert checkout_solution.checkout("ABCD") == 115