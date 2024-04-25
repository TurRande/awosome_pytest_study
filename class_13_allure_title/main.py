import pytest
import os

pytest.main(['--alluredir', 'allure_result', '--clean-alluredir'])


os.system('allure generate --clean ./allure_result -o ./allure_report')