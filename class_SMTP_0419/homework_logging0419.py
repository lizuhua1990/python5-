# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 13:13
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : homework_logging0419.py
# @Software: PyCharm
'''
4-19 smtp&logging
1:把发送邮件代码写成一个类，然后把这个类文件作为附件发给华华，邮箱：1255811581@qq.com

2:把你自己写的日志模块写成一个类，要求自己能够随时定义日志收集级别以及日志输出级别，要求同时输出到控制台以及指定文件。
1）级别指定，不管是日志收集还是日志输出，要求做成可配置（用到配置文件）
2）输入格式formatter,要求做成可配置，我想输出什么格式就是什么格式（用到配置文件）
'''

import logging
import configparser

class myLogger:
    def read_config (self,conf_path, section, option):
        tt = configparser.RawConfigParser()
        #configparser.ConfigParser() 会对%(asctime)s 解析为asctime，父类没有解析 所以用父类就好了
        tt.read (conf_path,encoding='utf-8')
        result = eval (tt.get (section, option,))
        return result

    def stleathlog(self):
        data=myLogger().read_config('logger.conf','LEVELFORMATTER','config')#取配置文件
        mylogger = logging.Logger ('stleath_log', 'DEBUG')#创建自己的容器以及收集等级
        hh = logging.StreamHandler ()  # 指定日志输出到控制台
        hh.setLevel (data['level'])#设置输出等级
        tt = logging.FileHandler ('mylogs.txt', 'a', encoding='utf-8')  # 写入指定文件，a表示追加
        tt.setLevel (data['level'])#设置输出等级
        formatter = logging.Formatter (data['formatter'])#设置一个格式，从配置文件中读取
        hh.setFormatter (formatter)
        tt.setFormatter (formatter)
        mylogger.addHandler (hh)
        mylogger.addHandler (tt)


        mylogger.debug('凉凉')#默认过滤-------》print()
        mylogger.info('成都秀')#默认过滤
        mylogger.warning('左左')
        mylogger.error('解冻打捞')
        mylogger.critical('华华')

if __name__ == '__main__':
    myLogger().stleathlog()





'''
logging.basicConfig函数各参数:
filename: 指定日志文件名
filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
 %(levelno)s: 打印日志级别的数值
 %(levelname)s: 打印日志级别名称
 %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
 %(filename)s: 打印当前执行程序名
 %(funcName)s: 打印日志的当前函数
 %(lineno)d: 打印日志的当前行号
 %(asctime)s: 打印日志的时间
 %(thread)d: 打印线程ID
 %(threadName)s: 打印线程名称
 %(process)d: 打印进程ID
 %(message)s: 打印日志信息
datefmt: 指定时间格式，同time.strftime()
level: 设置日志级别，默认为logging.WARNING
stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略
'''
