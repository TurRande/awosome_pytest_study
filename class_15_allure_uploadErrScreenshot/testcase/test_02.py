import allure


@allure.feature("模块2")
@allure.story("测试用例-Test类中所有")
class Test01:

    def test004(self):
        with allure.step("步骤4"):
            print("这是测试步骤4")
            with allure.step("步骤4.1"):
                print("这是测试步骤4.1")
            with allure.step("步骤4.2"):
                print("这是测试步骤4.2")
        print("这是测试用例4")

    def test005(self):
        with allure.step("步骤5"):
            print("这是测试用例5")

    def test006(self):
        with allure.step("步骤6"):
            print("这是测试用例6")


@allure.feature("模块3")
def test006():
     print("这是测试用例7")
     a = 2
     b = 3
     assert a + b == 4