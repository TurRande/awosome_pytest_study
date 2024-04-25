import pytest

"""
pip install pytest-html   命令行执行,安装pytest-html   https://pypi.tuna.tsinghua.edu.cn/simple
在report文件下,有一个assets的样式文件,这样的话,样式和报告是分离的
删除后,report.html就没有css样式了.
如果想样式和报告不分离.把assets的文件删除后,再main中添加"--self-contained-html",执行后,
报告中的样式也存在,也不会有assets文件出现
"""

# pytest.main(["-vs"])
pytest.main(["--html=report/report.html", "--self-contained-html"])
