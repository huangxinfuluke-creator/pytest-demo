
import pytest
from common.calculator import Calculator

@pytest.mark.parametrize(
	"a,b,expected",
	[
		pytest.param(1, 2, 3, id="normal"),
		pytest.param(1.2, 2.3, 3.5, id="float"),
		pytest.param("slut", " bitch", "slut bitch" , id="str"),

	]
)

def test_add1(a,b,expected,func_fixture, module_fixture, session_fixture):
	calc = Calculator()
	result = calc.add(a,b)
	assert result == expected

def test_add(func_fixture, module_fixture, session_fixture):

	calc = Calculator()
	result = calc.add(1,2)
	assert result == 3

def test_bitch(func_fixture, module_fixture, session_fixture):
	result = "bitch"
	assert result == "bitch"