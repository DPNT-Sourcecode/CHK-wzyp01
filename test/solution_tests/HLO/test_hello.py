from solutions.HLO import hello
import pytest

class TestHello():
    def test_hello(self):
        assert hello("a") == "Hello, World!"