import logging
import configparser
class userlogging:
    def loggingOut(self,S_Level,G_Level,formatter=None):
        my_logger=logging.Logger("DSDK")#创建收集器
        my_logger.setLevel(S_Level)#设置收集器的收集级别`
        sh=logging.StreamHandler()#指定日志输出到控制台
        sh.setLevel(G_Level)
        #fh=logging.FileHandler("log.txt",encoding="utf-8")#指定日志输出到文件
        #fh.setLevel(G_Level)
        #设置格式
        formatter_1=logging.Formatter(formatter)#格式化输出
        sh.setFormatter(formatter_1) #控制台日志添加格式化输出
        #fh.setFormatter(formatter_1)#文件日志增加控制台输出
        #对接收集器
        my_logger.addHandler(sh)
        #my_logger.addHandler(fh)
        return my_logger


def read_conf():
    cf=configparser.RawConfigParser()
    cf.read(r"G:\pythonxiangmu1\interface_auto_cases\config\registerconf.conf",encoding="utf-8")
    S_Level=eval(cf.get("LEVEL","S_Level"))
    G_Level=eval(cf.get("LEVEL","S_Level"))
    formatter_1=cf.get("FORMATTER","formatter_1")
    my=userlogging().loggingOut(S_Level[0],G_Level[0],formatter_1)
    return my

