import allure


@allure.step("步骤1")
def step_001():
    print("用例test_001正在被运行")


@allure.step("步骤2")
def step_002():
    print("用例test_002正在被运行")


@allure.step("步骤3")
def step_003():
    print("用例test_003正在被运行")

def test_allstep():
    step_001()
    step_002()
    step_003()