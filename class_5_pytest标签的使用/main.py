import pytest

pytest.main(['-vs', '-m', 'smoke']) # -m 代表执行smoke的标签用例,执行后会显示有4个跳过了执行
