# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 20:23
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : unittest_2.py
# @Software: PyCharm

import unittest
from class_unittest_0410.class_unittest_yuanLi import  testHttpRequset

if __name__ == '__main__':

    #可不可以按照自己的想法执行对用用例呢
    #方法一：TestSuite 这个类
    suite=unittest.TestSuite()#实例
    suite.addTest(testHttpRequset('test_get_1'))#添加用例，只执行‘test_getRequest’的方法名
    #把你要测试的用例  实例化
    suite.addTest(testHttpRequset('test_post_1'))
    #调用其中的某一条用例就直接使用：suite.addTest

    #方法二：TestLoader
    #from class_unittest_0410 import class_unittest_yuanLi#只引用到了模块名
    loader=unittest.TestLoader()
    #从指定模块里面家族所有的用例
    from class_unittest_0410 import class_unittest_yuanLi
    suite.addTest(loader.loadTestsFromModule(class_unittest_yuanLi))#从指定的模块里面加载所有的用例
    suite.addTest(loader.loadTestsFromTestCase(testHttpRequset))#直接使用类名
    #suite.addTest(loader)

    #file 文件
    file=open('pyhton5.txt',"w+")
    #执行用例
    runner=unittest.TextTestRunner(stream=file, descriptions='python5', verbosity=2)
    #流stream  你的结果写到哪里去    descriptions  叫什么        详细程度：0是否成功，1那几条是否成功，2具体那一条用例执行的结果
    runner.run(suite)
