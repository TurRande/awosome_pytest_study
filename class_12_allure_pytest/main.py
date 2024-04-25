import pytest
import os
# pip install allure-pytest -i https://pypi.tuna.tsinghua.edu.cn/simple

"""
在report-html中,main命令为:
pytest.main(['--html=report/report.html', '--self-contained-html'])
"""


pytest.main(['--alluredir', 'allure_result', '--clean-alluredir'])
"""
allure:
--alluredir 是allure运行的结果存放在 'allure-result'
--clean-alluredir: 每次运行前,清除之前文件夹里的文件
"""

os.system('allure generate --clean ./allure_result -o ./allure_report')
"""
第二步: os命令,把allure_result的结果,用来生成allure_report的报告
电脑需要安装allure,不然本地无法识别allure命令, (在本地安装allure前,电脑也要需要安装java)
"""