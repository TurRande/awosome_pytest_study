import pytest

pytest.main(['-v', '-s'])

"""
当你运行了这段指令之后,它就会在你当前的这个运行指令的文件相对同级的目录下,
寻找test_ 开头或者 _test结尾的.py文件,同级中找不到,就再往下层找;
然后在文件中寻找test开头的函数,或者Test开头的类,再在用例中找test开头的函数;
将通过上述方案中找到的所有用例依次运行;
执行顺序为:同级中先找符合的py文件,再从文件夹中寻找,文件中从上到下一次寻找并执行
"""

"""
也可以用命令行执行pytest
命令行中,在文件夹下执行:
pytest === pytest.main([])
pytest -s === pytest.main(["-s"])
pytest  -s -v === pytest.main(["-s", "-v"])
pytest  -sv === pytest.main(["-sv"])
pytest  -vs === pytest.main(["-vs"])

"""

