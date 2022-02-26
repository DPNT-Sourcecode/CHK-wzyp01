from solutions.HLO import hello_solution
import pytest

class TestHello():
    def test_hello(self):
        assert hello_solution.hello("abc") == "Hello, abc!"

        with pytest.raises(TypeError):
            hello_solution.hello(1)