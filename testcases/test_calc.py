import pytest
# from common.calculator import Calculator
from data.calc_data import add_test_data, sub_test_data


# @pytest.fixture
# def calc():
#     return Calculator()

@pytest.mark.smoke
@pytest.mark.parametrize("a,b,expected", add_test_data)
def test_add(calc, a, b, expected):
    print('calc.add(a,b)+smoke')
    assert calc.add(a, b) == expected

@pytest.mark.regression
@pytest.mark.parametrize("a,b,expected", sub_test_data)
def test_sub(calc, a, b, expected):
    assert calc.sub(a, b) == expected