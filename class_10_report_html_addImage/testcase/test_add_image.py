import pytest_html.extras
from pytest_html import extras
import pytest


def test_add_img(extra):   # extra ---> pytest的默认外部数据列表
    extra.append(pytest_html.extras.image("/Users/mac/PycharmProjects/pythonProject/pytest/class_10_report_html_addImage/imgdata/img.png", name="截图"))
#     def image_to_base64(image_path):
#         import base64
#         """这个函数是将图片转换成base64数据"""
#         with open(image_path, "rb") as image_file:
#             encoded_string = base64.b64decode(image_file.read())
#             return encoded_string.decode('ISO-8859-1')
#             # return encoded_string.decode('utf-8')
#
#
#     ## 添加图片文件夹
#     image_path = "/Users/mac/PycharmProjects/pythonProject/pytest/class_10_report_html_addImage/imgdata/img.png"  # 这里可以换成自定义图片路径
#     extra.append(extras.jpg(image_path))   # 添加图片,这个方法可以直接使用
#     #
#     # 添加base64格式的图片
#     base64_data = image_to_base64(image_path)
#     extra.append(extras.image(base64_data))   # 添加图片, 这个方法加载不出来图片
