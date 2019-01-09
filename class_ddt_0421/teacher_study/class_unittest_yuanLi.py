# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 20:00
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class_unittest_yuanLi.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 20:00
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class_unittest_yuanLi.py
# @Software: PyCharm

import unittest
import requests
from ddt import ddt,data,unpack
import copy

class siMida:
    dict={}
    list=[]
    def __init__(self,address):
        self.address=address#初始化函数
    def luJin(self):
        with open(self.address,'r') as file:#打开路径地址
            for i in file.readlines():#依次读取每一行内容记为:i
                for ii in i.strip ("\n").split (','):#每次读取的内容删除换行符，再根据“，”进行切割后记为：ii
                    self.dict[ii.split(':',1)[0]] = ii.split(':',1)[1]
                self.list.append(copy.deepcopy(self.dict))#每次从dict里面拷贝的值，插入list
        return self.list#返回值
t = siMida ('test.txt')
#print (t.luJin ())
#print('\n')
test_data = t.luJin ()

class httpRequest:
    def httpGet(self,url,data_1):
        request=requests.get(url,data_1)
        return request.json()
    def httpPost(self,url,data_1):
        request=requests.post(url,data_1)
        return request.json()

@ddt
class testHttpRequset(unittest.TestCase):
    def setUp(self):
        print("============我要开始测试了===============")

    def __init__(self,url,data_1,methodName):
        self.url=url
        self.data_1=data_1
        super(testHttpRequset,self).__init__(methodName)

    #@data(*test_data)
    #@unpack
    def test_get(self):#测试get方法  注册成功
        #url=a['url']#@data
        #a.pop('url')
        #hh={'mobilephone':mobilephone,'pwd':pwd}
        data=httpRequest().httpGet(self.url,self.data_1)
        print(data)
        print("这是第一条！")
        self.assertEqual (data['code'],'10001')
        self.assertEqual (data['msg'], '登录成功')

    #@data (*test_data)
    #@unpack
    def test_post(self):#测试post方法  注册成功
        #url=a['url']#@data
        #a.pop('url')
        #hh={'mobilephone':mobilephone,'pwd':pwd}
        data=httpRequest().httpGet(self.url,self.data_1)
        print (data)
        print("这是第二条！")
        self.assertEqual (data['code'],'10001')
        self.assertEqual (data['msg'], '登录成功')


    def tearDown(self):
        print("===============我要结束测试了！==================")

if __name__ == '__main__':
    unittest.main()









