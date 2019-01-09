# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 23:56
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : main.py
# @Software: PyCharm


import unittest
import os
from HtmlTestRunnerJT import HTMLTestRunner

suite=unittest.TestSuite()

testcase_dir=os.getcwd()+'/TestCases'
testreport_dir=os.getcwd()+'/TestReport'

suite.addTest(unittest.TestLoader().discover(testcase_dir))

fp=open(testreport_dir+'/Web_autoTest_report.html','wb')
runner=HTMLTestRunner(stream=fp,title='QCD_web单元测试报告',description='QCD_web单元测试报告',)

runner.run(suite)






