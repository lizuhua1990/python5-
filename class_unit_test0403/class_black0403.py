# -*- coding: utf-8 -*-
# @Time    : 2018/4/4 19:01
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 0403.py
# @Software: PyCharm

#在pycharm中是自动补全的变量的类别
# p:parameter 参数
# m:method    方法
# c:class     类
# v:variadle  变量
# f:function  函数


#错误问题：
#1、使用自己的名字、日期、用一些莫名其妙的名称 去命名变量、命名py文件、类
#2、拜托不要用  关键字去命名啊   http   requests  readlines等等
#3、如果你要引用第三方模块  请先安装好在调用 pip install ***
import requests
#写一个类、类里面有两个函数  一个完成get请求  一个完成post请求
class  httpRequest:
    def __init__(self,url,data):#初始化函数
        self.url=url
        self.data=data

    def getRequest(self,):#写函数
        result=requests.get(self.url,self.data)
        return result

    def postRequest(self,):#写函数
        result=requests.post(self.url,self.data)
        return result

#搞清楚继承
class Add:
    def  add(self,a,b):
        return a+b

class Sub(Add):#全继承
    def sub(self,a,b,c):
        result=self.add(a,b)#这个啥意思？调用父类Add的函数
        return result-c
