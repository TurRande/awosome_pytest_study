import pytest


@pytest.fixture()
def data():
    """
    conftest中的函数,用装饰器@pytest.fixture装饰后,可以把返回值赋值给testcase中的test用例
,前提是要在函数()中引用这个方法

    :return:[1, 2, 3, 4, 5]
    """
    return [1, 2, 3, 4, 5]


"""
装饰器,autouse=True作用为在每条测试用例执行之前或后自动调用, 
scope=为自动调用的级别,module代表模块级别,即每个py文件运行一次,同样的还有类"class"等等
"""


@pytest.fixture(autouse=True, scope="session")
def auto_use():
    """
    # scope=
        "module模块/
        session会话,多个文件只运行一次
        class一个类只调用一次
        function,默认值 一个函数调用一次
    :return:
    """
    print("这是自动调用的前置")
    yield
    print("这是自动调用的后置")
