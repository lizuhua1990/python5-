# -*- coding: utf-8 -*-
# @Time    : 2018/class_objcet_class0327-0329/16 21:53
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : homework0315.py
# @Software: PyCharm

#class_objcet_class0327-0329-15 Python函数&os
#注意，写函数，写函数！

class work_day5():
    def sub1(self):
#1、写函数，将姓名、性别，城市作为参数，并且性别默认为f(女)。
# 如果城市是在长沙并且性别为女，则输出姓名、性别、城市，并返回True,否则返回False。
        sex1 = ""
        def message (name, city, sex="f"):
            while city == "长沙" and sex == "f":
                sex1 = "女"
                print("Ture",name,sex1, city )
                exit()
            print("False")
        message(input("请输入名字："), input("请输入城市："), input("请输入性别（m表示男性，f表示女性）："))

        '''
#课堂讲解：
    def newDict(str,dict):#key value
        if str not in  dict.values():
            dict[str]=str
        return dict
    result=newDict("cs",{"name":"summer"})
    print(result)'''





#2、写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容,并将新内容返回
    def sub2(self):
        def panDuan(list):
            len_list = len(list)
            if len_list > 2:
                print("列表长度大于2")
                list_2 = list[0:2]
                print(list_2)
                return list_2
        panDuan(input("请输入你的列表："))

#class_objcet_class0327-0329、定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，
# 如果字符串不在字典中，则添加到字典中，并返回新的字典。
    def sub3(self):
        dict1 = {}
        def panDuan1(dict):
            dict1[dict] = dict
            print(dict1)
            a = input("请传入一个字符串‘’：")
            if a not in dict1:
                print("字符串不是字典中的值！")
                #exit()
                dict1[a] = a
            print(dict1)
            return dict1.values()
        panDuan1(dict = input("请传入一个字典值｛｝："))


#4、写一个函数，完成下面的功能：指定一个路径，读取所有的文件（file），
# 直到文件夹里面没有文件夹为止。先定位思想，然后动笔写。
#思路：1）迭代函数：函数内部自己调用自己。
#      2)os.path.conf.isdir  os.path.conf.isfile  os.listdir
#      class_objcet_class0327-0329）for 循环进行遍历

    def sub4(self):
        import os
        def luJin(address):
            for i in os.listdir(address):
                print(i)
        luJin(input("请输入指定路径格式(D:\python5)："))

        '''
#课堂讲解：
import os
def printAllPath(path.conf):
    all_dir=os.listdir(path.conf)#返回的是列表的数据
    print(all_dir)
    for dir in all_dir:
        new_path=os.path.conf.join(path.conf,dir)
        if os.path.conf.isfile(new_path):
            print("这个路径是文件，没有文件夹",new_path)
        else:
            print(new_path)
            printAllPath(new_path)#自己调用自己
printAllPath("D:\python5")
'''

if __name__ == '__main__':
#    work_day5.sub1(work_day5)
#    work_day5.sub2 (work_day5)
#    work_day5.sub3 (work_day5)
    work_day5.sub4 (work_day5)