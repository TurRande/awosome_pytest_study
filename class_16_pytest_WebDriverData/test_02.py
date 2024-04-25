import pytest

@pytest.mark.parametrize("num1, num2, excepted", [(1, 2, 3), (2, 3, 5), (3, 4, 7)])
def test02(num1, num2, excepted):
    print("{0}+{1} = {2}".format(num1, num2, excepted))
    assert num1 + num2 == excepted