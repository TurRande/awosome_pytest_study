import pytest


@pytest.fixture(params=[(1, 2, 3), (2, 3, 5), (3, 4, 7)], name="data_list")
def paramsdata(request):
    return request.param
