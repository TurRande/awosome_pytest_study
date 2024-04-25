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
            """失败截图数据"""
            ## 添加图片文件夹
            image_path = "/Users/mac/PycharmProjects/pythonProject/pytest/class_11_getReportResultAndScreenshot/imgdata/img.png"  # 这里可以换成自定义图片路径
            extra.append(extras.image(image_path))  # 添加图片,这个方法可以直接使用
    report.extra = extra