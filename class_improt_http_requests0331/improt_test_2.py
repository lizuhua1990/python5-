# -*- coding: utf-8 -*-
# @Time    : 2018/3/31 20:49
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : test.txt.py
# @Software: PyCharm


def  printMsg_2():
    print("我是improt_2下test_2")

#printMsg_2()
#import  引入方法
import class_improt_http_requests0331.improt_test_1
print("第一种调用方法")
class_improt_http_requests0331.improt_test_1.printMsg_1()

print("\n")
#from....improt  引入方法
from class_improt_http_requests0331.improt_test_1 import printMsg_1
print("第二种调用方法")
printMsg_1()

print("\n")
#调用improt_test_3
from class_improt_http_requests0331.improt_test_3 import addMethod
print("这是调用的improt_test_3")
e=addMethod()
e.printMsg_3()