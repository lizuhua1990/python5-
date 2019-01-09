# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 20:00
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class_unittest_yuanLi.py
# @Software: PyCharm

import unittest
import requests
class httpRequest:
    def httpGet(self,url,data_1):
        request=requests.get(url,data_1)
        return request.json()
    def httpPost(self,url,data_1):
        request=requests.post(url,data_1)
        return request.json()

class testHttpRequset(unittest.TestCase):
    def setUp(self):
        print("============我要开始测试了===============")

    def __init__(self,url,data_1,methodName):
        self.url=url
        self.data_1=data_1
        super(testHttpRequset,self).__init__(methodName)

    def test_get(self):#测试get方法  注册成功
        data=httpRequest().httpGet(self.url,self.data_1)
        print(data)
        print("这是第一条！")
        self.assertEqual (data['code'],'10001')
        self.assertEqual (data['msg'], '登录成功')

    def test_post(self):#测试post方法  注册成功
        data=httpRequest().httpGet(self.url,self.data_1)
        print (data)
        print("这是第二条！")
        self.assertEqual (data['code'],'10001')
        self.assertEqual (data['msg'], '登录成功')

    def tearDown(self):
        print("===============我要结束测试了！==================")

if __name__ == '__main__':
    unittest.main()

#import unittest 引入单元测试模块 具体原理
#1、写用例 2、加载集成用例 3、执行用例 4、出测试报告
#1、TestSuite

#2、TextTestRunner
#3、TestLoader

#3、TextTestRessult

#1、TestResuult



#6、TestCase




