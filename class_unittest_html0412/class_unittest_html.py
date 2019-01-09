# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 15:16
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class_unittest_html.py
# @Software: PyCharm

import time
from HTMLTestRunnerNew import HTMLTestRunner
import unittest
from class_unittest_0410.class_unittest_yuanLi import  testHttpRequset
from class_unit_test0403.class_unit_test1 import testMathMethod

if __name__ == '__main__':

    #可不可以按照自己的想法执行对用用例呢
    #方法一：TestSuite 这个类
    suite=unittest.TestSuite()#实例
    suite.addTest(testHttpRequset('test_get_1'))#添加用例，只执行‘test_getRequest’的方法名
    #把你要测试的用例  实例化
    #suite.addTest(testHttpRequset('test_post_1'))
    #调用其中的某一条用例就直接使用：suite.addTest

    #方法二：TestLoader
    #from class_unittest_0410 import class_unittest_yuanLi#只引用到了模块名
    loader=unittest.TestLoader()
    #从指定模块里面家族所有的用例
    from class_unittest_0410 import class_unittest_yuanLi
    suite.addTest(loader.loadTestsFromModule(class_unittest_yuanLi))#从指定的模块里面加载所有的用例
    #suite.addTest(loader.loadTestsFromTestCase(testMathMethod))#直接使用类名
    #suite.addTest(loader)

    #为了使生成文件同名不会被覆盖，用时间搓
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    #file 文件
    file=open(now+'python5.html',"wb+")

    # 利用 HTML 模版去出出具报告
    runner=HTMLTestRunner(stream=file, verbosity=2, title='python TextReport', description='现在应该萌萌哒')
    #流stream  你的结果写到哪里去    descriptions  描述叫什么    title  标题抬头
    #verbosity 详细程度：0是否成功，1那几条是否成功，2具体那一条用例执行的结果
    runner.run(suite)

















