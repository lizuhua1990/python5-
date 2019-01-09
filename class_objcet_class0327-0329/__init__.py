# -*- coding: utf-8 -*-
# @Time    : 2018/class_objcet_class0327-0329/28 21:30
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : __init__.py.py
# @Software: PyCharm

# 课堂讲解D:\python5\class_objcet_class0327-0329\test_data_1.txt
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


    #class_objcet_class0327-0329.把切割后的列表编程字典，新切割的字典下需要再次遍历
        for i in range(len(result_2)):
            dict[result_2[i].split(":",1)[0]]=result_2[i].split(":",1)[1]
        list.append(dict)

    print(list)
    return list
luJin(address=input("请输入有效路径："))