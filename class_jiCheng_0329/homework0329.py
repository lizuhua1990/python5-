# -*- coding: utf-8 -*-
# @Time    : 2018/3/30 14:43
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : homework0329.py
# @Software: PyCharm


#把3月20号的第二题写成类，并且创建一个实例，完成调用~记得代码要高效简洁~思密达~
#txt中存了很多数据，一行为一个请求数据，怎么样才能把这些数据读取到并且存到list中。
#url:http://119.23.241.154:8080/futureloan/mvc/api/member/login,mobilephone:13760246701,pwd:123456
#url:http://119.23.241.154:8080/futureloan/mvc/api/member/login,mobilephone:15678934551,pwd:234555 形式如下：
#将文件的数据读取出来，并根据逗号隔断，将隔断的内容存进list里，且隔断之后的内容里，冒号前面为key，后面为value。
#D:\python5\class_jiCheng_0329\test_1.txt
import copy
class siMida:
    dict={}
    list=[]
    def __init__(self,address):
        self.address=address#初始化函数
    def luJin(self):
        with open(self.address,'r') as file:#打开路径地址
            for i in file.readlines():#依次读取每一行内容记为:i
                #print(i)
                for ii in i.strip ("\n").split (','):#每次读取的内容删除换行符，再根据“，”进行切割后记为：ii
                    #print(ii)
                    # 对切割后的内容根据第一个“：”进行切割；第一项为key，value为第二项；保存到一个dict里面
                    self.dict[ii.split(':',1)[0]] = ii.split(':',1)[1]
                # list append 动态dict会只存最后修改的一个dict值，因为存的是引用，只能用copy  拷贝dict
                self.list.append(copy.deepcopy(self.dict))#每次从dict里面拷贝的值，插入list
        #print(self.list)
        return self.list#返回值
s=siMida(input("地址："))
#print (s.luJin()[0]['url'])
#del s.luJin()[0]['url']
#del s.luJin()[1]['url']
s.luJin()[0].pop('url')
s.luJin()[1].pop('url')
print (s.luJin()[0])
print (s.luJin()[1])
#print(s.luJin())


'''
class siMida:
    def __init__(self,address):
        self.address=address

    def luJin(self):
        file = open (self.address, 'r')
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
    #luJin(address=input("请输入有效路径："))

s=siMida(address=input("请输入有效路径："))
s.luJin()



class HomeWork_0329:
    dic_mydic = {}
    dic_mydic2 = {}
    list_myList = []

    def work1(self,str_fileName):
        with open(str_fileName,"r") as file:
            for str1 in file.readlines():
                for str2 in str1.split(','):
                    self.dic_mydic[str2.strip("\n").split(':', 1)[0]] = str2.strip("\n").split(':', 1)[1]
                    # list append 动态dict会只存最后修改的一个dict值，因为存的是引用，只能深拷贝dict
                self.list_myList.append(copy.deepcopy(self.dic_mydic))
        return self.list_myList

objHomeWork = HomeWork_0329().work1("test_1.txt")
print(objHomeWork)
'''






