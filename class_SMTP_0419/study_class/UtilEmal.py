'''
发送邮件工具类
'''
import os
import sys
import smtplib
# from Utillogger import UtilLog
from class_SMTP_0419.study_class.UtilConfig import UtilConfig
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class UtilEmal:

    def __init__(self,fileName,str_section,str_option):
        # self.objLog = UtilLog()
        self.obj_msg = MIMEMultipart()
        # 初始化读取邮件配置文件中的数据
        self.dict_emalConf = eval(UtilConfig(sys.path[0] + '/config/' + fileName).getConfigData(str_section,str_option))
        self.subject = self.dict_emalConf ['subject']
        self.emalFrom = self.dict_emalConf ['from']
        self.emalTo = self.dict_emalConf ['to']
        self.mailType = self.dict_emalConf ['mailType']
        self.mailPort = self.dict_emalConf['mailPort']
        self.loginKey = self.dict_emalConf['loginKey']
        self.MIMEText = self.dict_emalConf['MIMEText']
        # self.objLog.wInfo('邮件配置初始化成功....')

    def setContext(self,context):
        # UtilLog().wInfo("test")
        self.obj_msg = MIMEMultipart()
        self.obj_msg['subject'] = self.subject
        self.obj_msg['from'] = self.emalFrom
        self.obj_msg['to'] = self.emalTo
        obj_puretext = MIMEText(context,'plain','utf-8')
        self.obj_msg.attach(obj_puretext)
        self.obj_msg.attach(self.addFile(sys.path[0] + '/' + os.path.basename(__file__)))
        # self.objLog.wInfo('写入邮件内容成功....')
        return str(self.obj_msg)

    def addFile(self,fileName):
        # 添加附件
        obj_File = MIMEApplication(open( fileName,'rb').read())
        obj_File.add_header('Content-Disposition', 'attachment', filename=os.path.basename(__file__))
        # self.objLog.wInfo('邮件添加附件成功....')
        return obj_File

    def sendEmal(self):
        obj_conn = smtplib.SMTP_SSL(self.mailType,self.mailPort)
        obj_conn.login(self.emalFrom,self.loginKey)
        try:
            obj_conn.sendmail(self.emalFrom,self.emalTo,self.setContext(self.MIMEText))
            # self.objLog.wInfo('邮件发送成功....')
        except Exception as e:
            # self.objLog.wError('邮件发送失败... 失败原因：%s'%e)
            print(e)
        obj_conn.quit()

if __name__ == '__main__':
    UtilEmal('smtpconf.conf','STMPMASSAGEMIAL','config').sendEmal()
