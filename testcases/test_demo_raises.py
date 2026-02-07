import pytest


def divide(a, b):
    return a / b

def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("only numbers are allowed")
    return a + b

def test_add_string():
    with pytest.raises(TypeError, match="only numbers"):
        add("slut", "bitch")


@pytest.mark.parametrize(
    "a,b",
    [
        (10, 0),
        (5, 0),
        (100, 0),
    ]
)
def test_divide_invalid(a, b):
    with pytest.raises(ZeroDivisionError):
        divide(a, b)

