# -*- coding: utf-8 -*-
# @Time    : 2018/class_objcet_class0327-0329/18 20:46
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : file_open.py
# @Software: PyCharm


#file = open("test_data.txt","w")
#在你打开文件的时候 光标在头部


#print(file.name)
#print(file.closed)

#mode
#"r"---只读打开方式
#“r+”打开一个文件用于读写
#‘w’打开一个文件只用于写入
#‘w+’打开一个用于读写
#‘a’打开一个文件用于追加
#‘a+’打开一个文件用于读写
#、、、
'''

#python
#疑问？如果是中文呢？

#1、她是从头部开始读取的
# 2、根据你传入的长度来读取字符的
#class_objcet_class0327-0329、不传长度就默认读取左右值

print(file.read())#读的操作
print(file.read(4))#值表示读取长度，从头部开始读取
print(file.tell())

print(file.read(5))#读取后续长度
print(file.tell())


#写操作
file.write("hh6666666")

print(file.tell())
print(file.read())
file.close()#关掉当前文件

#覆盖写  读写可以同步进行
'''
#file = open("test_data1.txt","r+")
#12345678910111213
#file.write('python joker is best!!')
#file.write("6")
#list_1 = ['1\n','2','class_objcet_class0327-0329','4','5','test.txt']
#file.writelines(list_1)
#result_1 =file.readline()
#print(result_1)

#result_1 = file.readlines()
#print(result_1)
#for item in result_1:
#    print(item.strip('\n'))
#
#print(file.read(5))
#print(file.tell())
#file.seek(class_objcet_class0327-0329,2)
#print(file.read())
#file.close()

#r  只读  光标在最前面
#r+  读写  必须文件存在  写覆盖对应长度的内容

#w 只写 文件不存在  直接新建一个写入文件
#如果文件存在 直接清除原文内容在写入

#w+ 读写 文件不存在  直接新建一个写入文件
#如果文件存在 直接清除原文内容在写入
#可以读  但是根据光标的位置来决定位置的读取内容


#file.seek (offset[, whence])
#设置文件当前位置


def add(a,b):
    print("这是一个加法")
    return a+b
def sub(a,b):
    print("这是减法")
    c=add(a,b)
    print("我的上面调用了加法，结果是%d"%c)
    return c-a









