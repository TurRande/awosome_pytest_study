import pytest


# @pytest.fixture(params=["a", "b", "c"])
# def params(request):
#     return request.param

@pytest.fixture(params=["a", "b", "c"], name='abc')   # name= 可以自定义,不自定义的时候,在test中直接写params就行
# request是关键字，不能随意更改
def params(request):
    return request.param