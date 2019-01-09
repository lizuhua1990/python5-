# -*- coding: utf-8 -*-
# @Time    : 2018/4/4 22:05
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : homework0403.py
# @Software: PyCharm


#4-3 单元测试（一）

#1：测试数据如下：
#url='http://119.23.241.154:8080/futureloan/mvc/api/member/register'
#data_1={"mobilephone":"18688009092","pwd":"123456"}
#data_2={"mobilephone":"18688009091","pwd":"123456"}
#利用3-31号写的httpRequest类，对这个request类里面get函数和post函数分别写一条用例，
# 并对测试结果进行断言函数比对，要自己思考用什么值去比对才能知道自己的请求是成功的？

#2：请一定要在清明期间好好复习 类与对象  类的继承（全继承 部分继承 超继承）、类继承后函数的调用。
#3：之前作业没有做完的，赶紧去做。
#4：好好预习单元测试的相关内容。

#测试地址：D:\python5\class_unit_test0403\test_1.txt

import unittest
import requests
import copy
class siMida:
    dict={}
    list=[]
    def __init__(self,address):
        self.address=address#初始化函数
    def luJin(self):
        with open(self.address,'r') as file:#打开路径地址
            for i in file.readlines():#依次读取每一行内容记为:i
                for ii in i.strip ("\n").split (','):
                    self.dict[ii.split(':',1)[0]] = ii.split(':',1)[1]
                self.list.append(copy.deepcopy(self.dict))
        #print(self.list)
        return self.list#返回值
s=siMida(input("文本路径地址："))

class httpRequest:
    def httpGet(self,url,data_1):
        request=requests.get(url,data_1)
        return request.json()
    def httpPost(self,url,data_2):
        request=requests.post(url,data_2)
        return request.json()

url = str (s.luJin ()[0]['url'])
ii=len(s.luJin())#取列表长度，即txt里面的行数
for i in range(ii):
    del s.luJin ()[i]['url']
data={}

class testHttpRequset(unittest.TestCase):
    def test_get_1(self):#测试get方法  注册成功
        data=httpRequest().httpGet(url,s.luJin ()[0])
        self.assertEqual (data['code'],'10001')
        self.assertEqual (data['msg'], '注册成功')
    def test_get_2(self):#测试get方法  手机号码已被注册情况
        data=httpRequest().httpGet(url,s.luJin ()[0])
        self.assertEqual (data['code'],'20110')
        self.assertEqual (data['msg'], '手机号码已被注册')
    def test_get_3 (self):  # 测试get方法  密码为空
        data = httpRequest ().httpGet (url, s.luJin ()[0])
        self.assertEqual (data['code'], '20103')
        self.assertEqual(data['msg'], '密码不能为空')
    def test_get_4 (self):  # 测试get方法  手机号码输入错误
        data = httpRequest ().httpGet (url, s.luJin ()[0])
        self.assertEqual(data['code'], '20109')
        self.assertEqual(data['msg'], '手机号码格式不正确')
    def test_get_5 (self):  # 测试get方法  手机号码为空
        data = httpRequest ().httpGet (url, s.luJin ()[0])
        self.assertEqual(data['code'], '20103')
        self.assertEqual(data['msg'], '手机号不能为空')
    def test_post_1(self):#测试post方法  注册成功
        data=httpRequest().httpPost (url,s.luJin ()[1])
        self.assertEqual (data['code'],'10001')
        self.assertEqual (data['msg'], '注册成功')
    def test_post_2(self):#测试post方法  手机号码已被注册情况
        data=httpRequest().httpPost (url,s.luJin ()[1])
        self.assertEqual (data['code'],'20110')
        self.assertEqual (data['msg'], '手机号码已被注册')

if __name__ == '__main__':
    unittest.main()
'''


#课堂讲解：
#断言：希望结果和实际结果进行对比
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
        self.url='http://119.23.241.154:8080/futureloan/mvc/api/member/register'
        self.data_1={'mobilephone':'15805281333','pwd':'234555'}

    def test_get_1(self):#测试get方法  注册成功
        data=httpRequest().httpGet(self.url,self.data_1)
        print(data)
        print("这是第一条！")
        self.assertEqual (data['code'],'10001')
        self.assertEqual (data['msg'], '注册成功')
    def test_get_2(self):#测试get方法  手机号码已被注册情况
        data=httpRequest().httpGet(self.url,self.data_1)
        print (data)
        print ("这是第二条！")
        self.assertEqual (data['code'],'20110')
        self.assertEqual (data['msg'], '手机号码已被注册')

    def test_post_1(self):#测试post方法  注册成功
        data=httpRequest().httpGet(self.url,self.data_1)
        print (data)
        print("这是第三条！")
        self.assertEqual (data['code'],'10001')
        self.assertEqual (data['msg'], '注册成功')

    def tearDown(self):
        print("===============我要结束测试了！==================")

#可不可以按照自己的想法执行对用用例呢


if __name__ == '__main__':
    unittest.main()

'''




"""
1：测试数据如下：
url='http://119.23.241.154:8080/futureloan/mvc/api/member/register'
data_1={"mobilephone":"18688009092","pwd":"123456"}
data_2={"mobilephone":"18688009091","pwd":"123456"}
利用3-31号写的httpRequest类，对这个request类里面get函数和post函数分别写一条用例，并对测试结果进行断言函数比对，要自己思考用什么值去比对才能知道自己的请求是成功的？


class HomeWork0403:
    def httpGet(self,url,data):
        request=requests.get(url,data)
        return request.json()
    def httpPost(self,url,data):
        request=requests.post(url,data)
        return request.json()

class MyTestCase(unittest.TestCase):
    obj_hw = HomeWork0403()
    str_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/register'
    str_data_1 = {"mobilephone": "18688009097", "pwd": "123456"}
    str_data_2 = {"mobilephone": "18688009090", "pwd": "123456"}
    str_data_3 = {"mobilephone": "", "pwd": "123456"}
    str_data_4 = {"mobilephone": "18688009090", "pwd": ""}
    str_data_5 = {"mobilephone": "16688009090", "pwd": "123456"}
    str_data_6 = {"mobilephone": "18688016497", "pwd": "123456"}

    #测试get方法 手机号码已被注册情况
    def test_httpGet1(self):
        dic_result = self.obj_hw.httpGet(self.str_url,self.str_data_1)
        self.assertEqual(dic_result['code'], '20110')
        self.assertEqual(dic_result['msg'], '手机号码已被注册')

    # 测试get方法 手机号码为空情况
    def test_httpGet2(self):
        dic_result = self.obj_hw.httpGet(self.str_url, self.str_data_3)
        self.assertEqual(dic_result['code'], '20103')
        self.assertEqual(dic_result['msg'], '手机号不能为空')

    # 测试get方法 密码为空情况
    def test_httpGet3(self):
        dic_result = self.obj_hw.httpGet(self.str_url, self.str_data_4)
        self.assertEqual(dic_result['code'], '20103')
        self.assertEqual(dic_result['msg'], '密码不能为空')

    # 测试get方法 手机号码输入错误情况
    def test_httpGet4(self):
        dic_result = self.obj_hw.httpGet(self.str_url, self.str_data_5)
        self.assertEqual(dic_result['code'], '20109')
        self.assertEqual(dic_result['msg'], '手机号码格式不正确')

    # 测试get方法 注册成功情况
    def test_httpGet5(self):
        global dic_result
        dic_result = self.obj_hw.httpGet(self.str_url, self.str_data_6)
        self.assertEqual(dic_result['code'], '10001')
        self.assertEqual(dic_result['msg'], '注册成功')

    # 测试post方法 手机号码已被注册情况
    def test_httpPost(self):
        global dic_result
        dic_result = self.obj_hw.httpPost(self.str_url, self.str_data_2)
        self.assertEqual(dic_result['code'], '20110')
        self.assertEqual(dic_result['msg'], '手机号码已被注册')

if __name__ == '__main__':
    unittest.main()
    
"""
