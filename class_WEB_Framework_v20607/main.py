# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 23:56
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : main.py
# @Software: PyCharm

#unittest的执行方法
# import unittest
# import os
# from HtmlTestRunnerJT import HTMLTestRunner
#
# suite=unittest.TestSuite()
#
# testcase_dir=os.getcwd()+'/TestCases'
# testreport_dir=os.getcwd()+'/TestReport'
#
# suite.addTest(unittest.TestLoader().discover(testcase_dir))
#
# fp=open(testreport_dir+'/Web_autoTest_report.html','wb')
# runner=HTMLTestRunner(stream=fp,title='QCD_web单元测试报告',description='QCD_web单元测试报告',)
#
# runner.run(suite)


#pytest的执行方法
import pytest

pytest.main(['-m','smoke','--html','TestReport/report.html','--junitxml','TestReport/report.xml','TestCases'])





'''仍然想使用unittest的童鞋，给大家推荐几种过滤测试用例的方法，虽然没有yptest灵活，但是也挺实用，亲测可行
@unittest.skip(reason):无条件跳过测试，reason描述为什么跳过测试
@unittest.skipif(conditition,reason):condititon为true时跳过测试
@unittest.skipunless(condition,reason):condition不是true时跳过测试'''





