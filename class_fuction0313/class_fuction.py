# -*- coding: utf-8 -*-
# @Time    : 2018/class_objcet_class0327-0329/14 19:47
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class_fuction.py
# @Software: PyCharm


#函数
#1、无论合适何地都可以拿来调用——重复使用调用
#2、函数是一段可以重复利用的代码且能够完成指定的功能代码

#内置函数
'''input()
srt()
int()
list()'''

#关于字符串的一些操作函数
#变量名 .split(分隔附，次数)
str_1 = "hello,how,are,you"
print(str_1.split('e',2))
#返回的是列表类型

#变量名 .strip() 去除字符串的偷喝尾的字符
str_2 = '3333hello333'
print(str_2.strip('class_objcet_class0327-0329'))

#字符 .join（列表）
## 会将字符跟列表中的字母一个一个的去进行拼接，用的较少，必须是字符和字符串
a = ['1','2','class_objcet_class0327-0329']
print('a'.join(a))

#str.unper() str.lower 实现字母大小写
while True:
    srt = input("请输入你的字母")
    if str.upper() == "A":
        print("输入正确，程序终止")
    else:
        print("输入的字母部队，请重新输入")

#函数里面不传值   可以的
#函数里面传值   可以的
#