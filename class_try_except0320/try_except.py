# -*- coding: utf-8 -*-
# @Time    : 2018/class_objcet_class0327-0329/22 20:03
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : try_except.py
# @Software: PyCharm



#异常处理的语法：
'''
   try:
        XXXX
    except:
        XXXX
'''
try:#跟你要监控的代码
    #score = float (input ("请输入您的分数："))
    if 80 <= score <= 100:
        print ("优秀")
    elif 60 <= score <= 80:
        print ("及格")
    elif 0 <= score < 60:
        print ("不及格")
    elif score > 100 or score < 0:
        print ("你的分数有问题")
except BaseException as e:#捕捉出错并且处理错误
    print ("您输入非数字%s"%e)

finally:
    print("终于轮到我")#打开文件 打开数据库 打开文件流的情况下