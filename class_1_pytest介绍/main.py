import pytest

pytest.main(['-v', '-s'])

"""用例执行语句"""
"""
pytest main 里的[]表示用列表来接收执行时的参数
-s : 开启终端(控制台/输入台)的交互,如果不加就不能从控制台传入参数
-v: 让pytest的输出结果更加详细
"""
# pytest.main(["-s"])
# pytest.main([])
