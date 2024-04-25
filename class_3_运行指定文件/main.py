import pytest

# pytest.main(['-vs'])
# pytest.main(["testcase", "-vs"])
pytest.main(["testcase", "-vs"])

# 运行指定文件
# pytest.main(["test_01.py::Test01::test001", "-vs"])
# pytest.main(["testcase", "-vs"])
# pytest.main(["testcase/testcase", "-vs"])
# pytest.main(["testcase/testcase/test_01::Test01::test01", "-vs"])