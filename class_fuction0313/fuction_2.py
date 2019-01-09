# -*- coding: utf-8 -*-
# @Time    : 2018/class_objcet_class0327-0329/14 20:09
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : fuction_2.py
# @Software: PyCharm

#函数
#函授的语法
'''def function_name(参数1,参数2,参数3):
    #功能代码'''
#函数的名字命名：见明知意

#第一个简单的函数
#引入参数  位置参数
#位置参数可以多个
#默认参数必须放在位置参数的后面
#def PrintName(name = 'summer', age = 18):
def PrintName(name = input('请输入你的姓名：'), age = input("请输入你的年龄：")):
    print("我的名字是%s"%name + ',我今年', age, '岁')

#函数的引用
#如果你在定义这个函数的时候，规定有参数要穿进去的，
#那么引用函数的时候不能少
#默认值  在调用时候，如果存在可以不用输入
#有默认值参数，如果输入了值会替换掉默认值，如果没有就使用默认值
PrintName("长大", 22)


#练习：
#写一个函数，可以完成任意有序整数序列的数字相加  234   2+class_objcet_class0327-0329+4  1---10

def sum(m, n):
    sum = 0
    for i in range( m, n):
        sum = sum + i
    print(sum)
sum(1, 101)