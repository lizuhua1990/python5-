# -*- coding: utf-8 -*-
# @Time    : 2018/3/31 20:41
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : test.txt.py
# @Software: PyCharm

def  printMsg_1():
    print("我是improt_1下test_1")

#测试代码 程序执行的入口  当你加了这个之后，只有当前模块执行才会调用
if __name__=='__main__':
    printMsg_1()