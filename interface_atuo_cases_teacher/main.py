import unittest
import time
import HTMLTestRunnerNew
from interface_atuo_cases_teacher.public import run_interface_case

loader=unittest.TestLoader()
suite=unittest.TestSuite()
suite.addTest(loader.loadTestsFromModule(run_interface_case))

runner=unittest.TextTestRunner()
runner.run(suite)

now = time.strftime('%Y-%m-%d_%H_%M_%S')
with open(now + '_Test.html', 'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, title='测试报告V1.0', description='测试登录模块正常登录与用户名或密码错误用例', verbosity=2)
    runner.run(suite)
