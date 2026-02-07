import pytest
from common.calculator import Calculator

# session scope fixture
@pytest.fixture(scope="session")
def config():
    print("\n[session] setup: load config")
    cfg = {"env": "test"}
    yield cfg
    print("\n[session] teardown: release config")

# module scope fixture, 依赖 config
@pytest.fixture(scope="module")
def calc(config):
    print(f"\n[module] setup: create Calculator with env={config['env']}")
    calc_obj = Calculator()
    yield calc_obj
    print("\n[module] teardown: destroy Calculator")





@pytest.fixture(scope="function")
def func_fixture():
    print("\n[function scope] setup")
    yield
    print("\n[function scope] teardown")


@pytest.fixture(scope="module")
def module_fixture():
    print("\n[module scope] setup")
    yield
    print("\n[module scope] teardown")


@pytest.fixture(scope="session")
def session_fixture():
    print("\n[session scope] setup")
    yield
    print("\n[session scope] teardown")

