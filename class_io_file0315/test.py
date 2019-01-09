# -*- coding: utf-8 -*-
# @Time    : 2018/class_objcet_class0327-0329/22 19:47
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : test.txt.py
# @Software: PyCharm
'''
#课堂讲解：
def newDict(str,dict):#key value
    if str not in  dict.values():
        dict[str]=str
    return dict
result=newDict("cs",{"name":"summer"})
print(result)
'''




import os
def printAllPath(path):
    all_dir=os.listdir(path)#返回的是列表的数据
    print(all_dir)
    for dir in all_dir:
        new_path=os.path.join(path,dir)
        if os.path.isfile(new_path):
            print("这个路径是文件，没有文件夹",new_path)
        else:
            print(new_path)
            printAllPath(new_path)
printAllPath("D:\python5")