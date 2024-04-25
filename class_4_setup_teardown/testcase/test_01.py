def setup_function():
    """
    测试用例执行的前置操作
    应用范围为每个函数功能之前
    :return:
    """
    print("这是函数级别的前置操作")


def teardown_function():
    """
    测试用例执行的后置操作
    应用范围为每个函数功能之后
    :return:
    """
    print("这是函数级别的后置操作")


def setup_module():
    """
    测试用例执行的前置操作
    应用范围为每个test_开头的文件之前
    :return:
    """
    print("这是模块级别的前置操作")


def teardown_module():
    """
    测试用例执行的后置操作
    应用范围为每个test_开头的文件之后
    :return:
    """
    print("这是模块级别的后置操作")


def test001():
    print("这是测试用例001,正在被执行")


def test002():
    print("这是测试用例002,正在被执行")
