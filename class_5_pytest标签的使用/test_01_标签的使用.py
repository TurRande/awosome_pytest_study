import pytest


# mark.后面的标签可以自定义,在pytest.ini中进行声明
@pytest.mark.smoke
def test_login():
    # 登录测试用例
    print("01_login测试用例")


@pytest.mark.skip
def test_nihao():
    print("hello")
    print("02_hello测试用例")


@pytest.mark.smoke
def test_logout():
    print("03_logout测试用例")
    # 退出登录测试用例


@pytest.mark.smoke
@pytest.mark.regression
def test_sign():
    print("04_sign测试用例")


@pytest.mark.regression
def test_byebye():
    print("05_byebye测试用例")



