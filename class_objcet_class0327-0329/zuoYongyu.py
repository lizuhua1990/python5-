# -*- coding: utf-8 -*-
# @Time    : 2018/class_objcet_class0327-0329/28 22:16
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : zuoYongyu.py
# @Software: PyCharm

'''
#变量的声明
a= "test.txt"
print(a)

#函数里面的变量不声明可以吗
#形参--形式参数--占位置---调用这个函数的要传递两个参数
def add(a,b):
    return  a+b
    '''


#针对函数而言
#局部变量
#全局变量：函数外面---全局变量的作用域在整个py文件，所以函数可以直接调用

#1、全局变量的值我可以在函数内部进行修改么

#2、我一定要在内部修改全局变量呢？
B=6#全局 变量
def add():
    a=5#局部变量
    global B#2、解答：在全局变量声明后，在对全局变量继续赋值，就会修改全局变量
    B=0#1、解答：当你全局和局部有相同的变了的时候，优先调用内部变量，不会改变全局变量值
    print(a+B)

add()
print(B)

#class_objcet_class0327-0329、如果数据类型是 字典 列表的话  怎么办
#特殊点：listd的append方法， 可以改变全局变量
DICT={"name":"haha"}
LIST=[1,2,'677']

def printMsg():
    #global LIST#声明后会成为全局变量值
    # LIST.append('MILA')#listd的append方法， 可以改变全局变量
    LIST='xiaobai'#优先调用内部变量
    DICT["age"]=18
    print(LIST)
    print(DICT)

printMsg()
print(DICT)















