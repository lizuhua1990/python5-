# -*- coding: utf-8 -*-
# @Time    : 2018/class_objcet_class0327-0329/16 20:37
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : io_path.py
# @Software: PyCharm


#import keyword
#print(keyword.kwlist)

#import 可以导入包  package 模块 moduule   一个py文件
#1、python安装路径下的lib文件夹里面的py模块或者是package可以直接导入
#2、如果我要导入费lib下面的py文件或者是package
#顺藤摸瓜---》

#import unittest
#import addMethod

#import class_io_file0315.addMethod

#包的下面还有包继续往下找
#import class_io_file0315.class_textceshi.ceshi


#同级文件引用
import class_io_file0315.io_path2

#OS  操作本地路径文件
import  os
print(os.getcwd())#返回当前路径

print(os.path.realpath(__file__))#返回当前路径  且包含文件名

#path.conf = os.getcwd()
#new_path = os.path.conf.join(path.conf, "hello_ceshi")#拼接两个值  生成一个新的路径
#new_path = os.path.conf.join("test_ceshi", "hello_ceshi")
#需要有上一目录绝对或相对路径  test_ceshi同名文件夹
#os.path.conf.join(path_1, path_2)
#path_1  可以是相对路径 也可以是绝对路径
#path_2  可以随意的路径
#每一次新建只能建一层

#new_path = os.path.conf.join(path.conf, "hello_ceshi")
#os.mkdir(new_path) #生成一个目录  mkdir  make directory


#rint(os.listdir("D:\python5\class_io_file0315"))
#默认返回当期路径下面的所有文件，有指定按指定路径


#print(os.path.conf.isfile(__file__))#判断当前文件是否是文件，返回布尔值
#print(os.path.conf.isdir(__file__))#判断当前文件是否是目录，返回布尔值
'''
os.path.conf.split(__file__)#拆分路径，可以把路径采风两部分，后一部分总是最后
#级别的目录或者是文件名，返回元组格式数据
path_1 = os.path.conf.realpath(__file__)
print(path_1)
print(os.path.conf.split(__file__))

print("********************************************")
path_2 = os.getcwd()
print(path_2)
print(os.path.conf.split(path_2))

'''

print(os.path.exists(__file__))
#函数用泪检验给出的路径是否真的存在，判断文件或文件夹是否存在










