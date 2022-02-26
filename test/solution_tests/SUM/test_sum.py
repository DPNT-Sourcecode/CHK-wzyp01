from solutions.SUM import sum_solution
import pytest

class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

        with pytest.raises(ValueError):
            assert sum_solution.compute(-1, 1)

        with pytest.raises(ValueError):
            assert sum_solution.compute(1, -1)

        with pytest.raises(ValueError):
            assert sum_solution.compute(101, 1)

        with pytest.raises(ValueError):
            assert sum_solution.compute(1, 101)

        with pytest.raises(TypeError):
            assert sum_solution.compute(1.1, 2)

        with pytest.raises(TypeError):
            assert sum_solution.compute(2, 1.1)

        with pytest.raises(TypeError):
            assert sum_solution.compute("2", 1)

        with pytest.raises(TypeError):
            assert sum_solution.compute(1, "2")

