# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 22:52
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : homework0412.py
# @Software: PyCharm

"""
1：测试数据存在TXT里面，格式如下：
url:http://119.23.241.154:8080/futureloan/mvc/api/member/login,mobilephone:13760246701,pwd:123456,method:get
url:http://119.23.241.154:8080/futureloan/mvc/api/member/login,mobilephone:15678934551,pwd:234555,method:post
url:http://119.23.241.154:8080/futureloan/mvc/api/member/login,mobilephone:15678934551,pwd:2345588,method:get
url:http://119.23.241.154:8080/futureloan/mvc/api/member/login,mobilephone:15678934551,pwd:234599,method:post

期中method是http请求的方式，如果是get那么就调用get请求，如果是post就调用post请求

2：针对http请求去做写测试用例，就是对3月31号写的类去做单元测试，但是要求测试数据来自于第一步的txt里面，然后还会根据method去发起get请求或者是post请求。

3：执行测试用例，并且生成HTML报告
"""
#路径：D:\python5\class_unittest_html0412\test.txt
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
                for ii in i.strip ("\n").split (','):#每次读取的内容删除换行符，再根据“，”进行切割后记为：ii
                    self.dict[ii.split(':',1)[0]] = ii.split(':',1)[1]
                self.list.append(copy.deepcopy(self.dict))#每次从dict里面拷贝的值，插入list
        return self.list#返回值

    def httpGet (self, url, data_1):
        request = requests.get (url, data_1)
        return request.json ()

    def httpPost (self, url, data_1):
        request = requests.post (url, data_1)
        return request.json ()

    def doReq(self,dic_testDate):
        """
        请求操作，根据数据中的method不同调用不同的请求方法
        :param dic_testDate: luJin 方法返回的字典数据列表
        :return: 返回服务器处理的结果json格式数据
        """
        if dic_testDate['method'] == 'get':
            return self.httpGet(dic_testDate['url'],dic_testDate)
        if dic_testDate['method'] == 'post':
            return self.httpPost(dic_testDate['url'], dic_testDate)
        if dic_testDate['method'] not in ('get','post'):
            print("请求方式不存在...")
            return None

if __name__ == '__main__':
    t=siMida('test.txt')
    list=t.luJin()
    for str in list:
        print(t.doReq(str))


