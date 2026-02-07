import pytest

add_test_data = [
    pytest.param(1, 1, 2,id="1,1"),
    pytest.param(2, 3, 5,id="2,3"),
    pytest.param(10, 20, 30,id="10,20"),
]

sub_test_data = [
    pytest.param(5, 2, 3,id="5,2"),
    pytest.param(10, 5, 5,id="10,5"),
]
