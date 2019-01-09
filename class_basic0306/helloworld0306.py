# -*- coding: utf-8 -*-
# @Time    : 2018/class_objcet_class0327-0329/14 18:08
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : test_0313.py
# @Software: PyCharm

'''print("hell python5!!")


import  keyword
print(keyword.kwlist)

#字符串
str_1='hello world 1'
str_2="hello world 2"

#变量 x=1 x=2 y=z 左边是变量名 右边变量值
#等号的作用 把右边的只赋值给左边的变量名
#Python命名是有江湖规矩的  可以包含数字 字母 下划线
#python 不成文的江湖规矩：变量命名的时候  包括python文件名命名的时候 要见名知意


#关于换行符  以及转义字符 r R 帮你把普通字符变成普通的字符
print(R"hello world class_objcet_class0327-0329 \n hello python5期的同学 你们好")

#关于字符串的拼接 可以相加拼接
print(str_1+str_2)
print(str_1,str_2)



#注意：不能以数字开头
#3_str="hello world class_objcet_class0327-0329"



#常用数据类型 整数
a=1
b=1.6
c="666"

print(type(a))
print(type(b))
print(type(c))

#对不同类型的数据类型进行拼接  只能用逗号或者是强制转化下

#强制转化
a=1
b=1.11
c="666"
print(str(a)+c)

#str()  强制转换函数 把变量那个强制转化成 字符串格式的数据
#int()   把变量强制转化为 整数格式的数据
print(b)
print(int(b))

str_6="nice day!!!"
#字符串的截断  你可以根据每个字符所在的索引获取到对应的值
#Python 里面  数据的索引 排序 是从开始位置确定：n-1
#我想获取字符串厘米那的某个单字符  根据索引获取
print(str_6[7])


#现在我要获取多个字符或者是某一节字符
#有区域范围的  取前不取后
print(str_6[5:7])
print(str_6[5:8])

print(str_6[2:4])

#特殊的写法 获取nice这个单词
print(str_6[:4])
print(str_6[4:])

#倒序写法
print(str_6[:-1])
print(str_6[:-7])
print(str_6[-11:-7])
print(str_6[:])


a=input("请输入你的姓名:")
print(a[4])
#请你把输入的数据进行截断  取第五个字符

#布尔值  TURRE   FALSE

#格式化输出
name="请讲明白"
print("你的姓名是%s"%name)

#%s  %d
#从控制台获取的数据都是str 类型的
a=int(input("请输入喜欢数字："))
print("你最喜欢的数字是：%d",%a)'''


#%f  输出一个浮点数
c=6.666666
print("请输入浮点数%.2f"%c)#后两位四舍五入