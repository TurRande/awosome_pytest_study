import allure

@allure.feature("模块1")
@allure.story("测试用例1")
def test_001():
    print("用例test_001正在被运行")

@allure.feature("模块1")
@allure.story("测试用例2")
def test_002():
    print("用例test_002正在被运行")

@allure.feature("模块1")
@allure.story("测试用例3")
def test_003():
    print("用例test_003正在被运行")