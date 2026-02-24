import pytest
from common.calculator import Calculator
from api.simple_book_api import SimpleBookAPI
import time



@pytest.fixture(scope="session")
def token():
    api = SimpleBookAPI()
    email = f"pytest_{int(time.time())}@gmail.com"
    response = api.post_register_api_clients(
        client_email=email,
        client_name="luke"
    )
    print('返回token是：'+str(response.json()))
    if response.status_code not in [200, 201]:
        raise Exception(f"Token generation failed: {response.text}")

    token = response.json().get("accessToken")

    if not token:
        raise Exception("No access token returned")

    return token


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

