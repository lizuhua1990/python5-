# -*- coding: utf-8 -*-
# @Time    : 2018/class_objcet_class0327-0329/22 21:12
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : homework0320.py
# @Software: PyCharm

# Python IO/文件操作作业
class work_day7():
#1.txt里面存了很多数据，都是用逗号隔开的，一个逗号隔开的就是一个数据，
# 一个数据对应列表里面的一个元素。怎么样才能把这些数据读取到出来并且存到list中。
    def sub1(luJin):
        list_myList = []
        with open (luJin, "r") as file:
            list_myList = file.read ().split (',')
        print (list_myList)
        return list_myList
    sub1(luJin = str(input("请输入路径：")))


#2.txt中存了很多数据，一行为一个请求数据，怎么样才能把这些数据读取到并且存到list中。
#url:http://119.23.241.154:8080/futureloan/mvc/api/member/login,mobilephone:13760246701,pwd:123456
#url:http://119.23.241.154:8080/futureloan/mvc/api/member/login,mobilephone:15678934551,pwd:234555 形式如下：
#将文件的数据读取出来，并根据逗号隔断，将隔断的内容存进list里，且隔断之后的内容里，冒号前面为key，后面为value。

    def sub2(luJin_1):
        list_myList = []
        with open (luJin_1, "r") as file:
            for str1 in file.readlines ():
                str1 = str1.replace ("\n", "")
                # 根据逗号隔断
                for ii in str1.split (','):
                    # 将隔断的内容存进list里
                    list_myList.append (ii)
        print (list_myList)
        return list_myList

    sub2(luJin_1 = str(input("请输入路径：")))

#课堂讲解D:\python5\class_try_except0320\test_data_1.txt
'''
# 1.肯定是要需要通过open函授来读取内容，然后利用file对象里面readlines来读取数据
def luJin(address):
    file = open (address, 'r')
    result_1 = file.readlines ()
    print ("从txt里面获取的数据result_1", result_1)

# 2.进行切割，汽狗之前观察数据list里面的每一个数据都是字符串类型
# 因为要对每一个元素进行切割，所以要遍历
    list = []
    for item in result_1:
        result_2 = item.strip ("\n").split (',')
        print ("对file对象获取的每一行数据进行都好进行切割", result_2)
        dict = {}

#3.把切割后的列表编程字典，新切割的字典下需要再次遍历
        for i in range(len(result_2)):
            dict[result_2[i].split(":",1)[0]]=result_2[i].split(":",1)[1]
        list.append(dict)
    print(list)
    return list
luJin(address=input("请输入有效路径："))
'''

if __name__ == '__main__':
#    work_day7().sub1()
    work_day7().sub2()













