# -*- coding: utf-8 -*-
# @Time    : 2018/4/4 20:36
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : httpRequest.py
# @Software: PyCharm

import requests
class httpRequest:
    def __init__(self,url,data):
        self.url=url
        self.data=data
    def getRequest(self):
        result=requests.get(self.url,self.data)
        return result.json()
    def postRequest(self):
        result=requests.get(self.url,self.data)
        return result.json()

#请对httpRequest写测试用例
#对get请求写一条正常请求的，并对结果利用断言判断是否成功
#对post请求写一条正常请求的，并对结果利用断言判断是否成功
#测试数据如下：
#data_2={'status': 0, 'code': '20110', 'data': None, 'msg': '手机号码已被注册'}
url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/register'
data ={'mobilephone': '18678477555', 'pwd': '234555'}
data_1={}
import unittest
class testHttpRequset(unittest.TestCase):
    def test_get(self):
        t=httpRequest()
        data_1=t.getRequest(url,data)
        self.assertEqual ('20110',data_1['code'])
    def test_post(self):
        t=httpRequest()
        data_1=t.postRequest (url,data)
        self.assertEqual ('20110',data_1['code'])

if __name__ == '__main__':
    unittest.main()