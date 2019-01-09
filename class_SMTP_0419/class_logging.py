# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 16:06
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class_logging.py
# @Software: PyCharm

import logging#Python 自带的logging
#root logger  默认的存在的最高级别的日志收集器   warning级别以上的信息

#1、我要自立门户，自己建立一个日志容器
mylogger=logging.Logger('stleath_log','DEBUG')#自己创建一个收集容器
#mylogger.setLevel('DEBUG')#设置等级的级别

#2、还要建立一个属于自己的输出日志容器  过滤器  跟我们日志手机容器搭配使用
hh=logging.StreamHandler()#指定日志输出到控制台
hh.setLevel('INFO')#设置等级

#tt=logging.StreamHandler()
#tt.setLevel('DEBUG')

#指定日志输出到指定文件里面去
tt=logging.FileHandler('mylogs.txt','a',encoding='utf-8')#a表示追加
tt.setLevel('DEBUG')

#设置一个格式
formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

hh.setFormatter(formatter)
tt.setFormatter(formatter)
#3、既然要搭配使用，就要搭配对接使用
mylogger.addHandler(hh)
mylogger.addHandler(tt)#输出


#4、专门做输出处理的容器或者佳偶哦过滤器，只输出warning级别以上的信息
mylogger.debug('凉凉')#默认过滤-------》print()
mylogger.info('成都秀')#默认过滤
mylogger.warning('左左')
mylogger.error('解冻打捞')
mylogger.critical('华华')
'''
logging.debug('凉凉')#默认过滤
logging.info('成都秀')#默认过滤
logging.warning('左左')
logging.error('解冻打捞')
logging.critical('华华')
'''
#formatter:决定日志记录的最终输出格式
#formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

'''
def add(a,b):
    mylogger.info('第一个加数的值是：%s'%a)
    mylogger.info('第二个加数的值是：%s'%b)
    try:
        result=a+b
        mylogger.info('加数值是：%s'%result)
    except Exception as e:
        mylogger.error('加法出错了！,错误的是：%s'%e)
        raise e

add(1,'444')
'''
