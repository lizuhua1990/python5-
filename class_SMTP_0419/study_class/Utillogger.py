import sys
import time
import logging
from class_SMTP_0419.study_class.UtilConfig import UtilConfig

class UtilLog:
    def __init__(self):
        self.obj_conf = UtilConfig(sys.path[0]+'/config/' + 'LogConf.conf')
        self.log_names = self.obj_conf.getConfigData('log_name','name')
        self.log_level = self.obj_conf.getConfigData(self.log_names,'level')
        self.log_handlers = self.obj_conf.getConfigData(self.log_names,'handlers')
        self.consoleHandler_level = self.obj_conf.getConfigData('mylog_consoleHandler','level')
        self.outfileHandler_level = self.obj_conf.getConfigData('mylog_outfileHandler','level')
        self.mylog_formatter = self.obj_conf.getConfigData('mylog_formatter','format')
        self.mylog = logging.Logger(self.log_names,'CRITICAL')

    def getLog(self):
        # 当前日期格式化
        now = time.strftime('%Y-%m-%d')
        fm = logging.Formatter(self.mylog_formatter)
        sh = logging.StreamHandler()
        sh.setLevel(self.consoleHandler_level)
        sh.setFormatter(fm)
        fh = logging.FileHandler(sys.path[0]+'/log/'+ now + '.log','a',encoding='UTF-8')
        fh.setLevel(self.outfileHandler_level)
        fh.setFormatter(fm)
        self.mylog.addHandler(sh)
        self.mylog.addHandler(fh)
        return self.mylog

    def wDebug(self,strMsg):
        self.getLog().debug(strMsg)

    def wInfo(self,strMsg):
        self.getLog().info(strMsg)

    def wWarning(self,strMsg):
        self.getLog().warning(strMsg)

    def wError(self,strMsg):
        self.getLog().error(strMsg)

    def wCritical(self,strMsg):
        self.getLog().critical(strMsg)

if __name__ == '__main__':
    UtilLog().wInfo("test")

