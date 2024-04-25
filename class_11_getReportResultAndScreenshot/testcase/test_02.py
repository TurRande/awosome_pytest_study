def test_004():
    print("用例test_004正在被运行")


def test_005():
    print("用例test_005正在被运行")


def test_006():
    """
    assert 语句通过断言来触发异常
    :return:
    """
    print("这是一条异常用例")
    a = 1
    b = 2
    assert a + b == 4