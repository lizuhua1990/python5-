# -*- coding: utf-8 -*-
# @Time    : 2018/class_objcet_class0327-0329/22 20:49
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : try_except_2.py
# @Software: PyCharm

try:
    file = open("test_data_1.txt","r")#只读模式
    file.write('66666666')
    print(file.close)
except Exception as e:
    print("错误是%s"%e)
finally :
    print(file.closed)
    file.close()
    print(file.closed)

#上下文管理器------指明这个文件的作用范围
with open("test_data_1.txt","w") as file:
    file.write("3333333")















