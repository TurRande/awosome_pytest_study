import pytest


@pytest.fixture(autouse=True, scope="function")
def setupAndteardown():
    print('这是testcase里的[前置]')
    yield
    print('这是testcase里的[后置]')


@pytest.fixture(params=[1, 2, 3, 4], name='list')
def dataTest(request):
    return request.param