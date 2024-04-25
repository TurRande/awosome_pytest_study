import allure
import pytest
from pytest_html import extras


@pytest.hookimpl(hookwrapper=True)  # 写死的,pytest的钩子方法
def pytest_runtest_makereport(item, call):  # 写死的
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        print("用例执行结果:", report.outcome)
        if report.outcome != "passed":


            """失败截图数据,添加图片文件夹"""
            image_path = "/Users/mac/PycharmProjects/pythonProject/pytest/class_15_allure_uploadErrScreenshot/imgdata/img.png"
            """allure报告添加html的方法"""
            with open(image_path, "rb") as image_file:
                allure.attach(image_file.read(), name="可以自定义的图片名称", attachment_type=allure.attachment_type.PNG)
