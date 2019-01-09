# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 20:38
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : homework_2_0412.py
# @Software: PyCharm


import unittest
import time
from HTMLTestRunnerNew import HTMLTestRunner
from class_unittest_html0412.homework0412 import siMida

class WorkTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.obj_hw = siMida('test.txt')
        cls.list_dicDate = cls.obj_hw.luJin()

    def setUp(self):
        print(WorkTest.list_dicDate)

    def test_doReq1(self):
        for dic_date in WorkTest.list_dicDate[0:2]:
            print("本次用例使用%s请求方式" % (dic_date['method']))
            dic_result = WorkTest.obj_hw.doReq(dic_date)
            self.assertEqual(dic_result['code'], '10001')
            self.assertEqual(dic_result['msg'], '登录成功')

    def test_doReq2(self):
        for dic_date in WorkTest.list_dicDate[2:4]:
            print("本次用例使用%s请求方式" % (dic_date['method']))
            dic_result = WorkTest.obj_hw.doReq(dic_date)
            self.assertEqual(dic_result['code'], '20111')
            self.assertEqual(dic_result['msg'], '用户名或密码错误')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(WorkTest))
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    with open(now+'_Test.html', 'wb+') as htmlReport:
        runner = HTMLTestRunner(stream=htmlReport,title='测试报告V1.0',description='测试登录模块正常登录与用户名或密码错误用例',verbosity=2)
        runner.run(suite)