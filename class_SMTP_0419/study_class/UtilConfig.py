"""
config 配置文件操作工具类
"""
import sys
# import Utillogger
from configparser import *

class UtilConfig:
    def __init__(self,fileName):
        # 创建配置文件对象
        self.obj_config = RawConfigParser()
        # Utillogger.UtilLog().wInfo('开始配置文件初始化操作...')
        self.str_confFileName = fileName
        self.obj_config.read(self.str_confFileName, encoding='UTF-8')

    def getConfigData(self, str_section, str_option):
        """
        读取conf配置文件操作
        :param str_section: conf文件section的名称 [ XXX ]
        :param str_option:  conf文件option的名称（key）
        :return: 返回key 对应的 value
        """
        # UtilLog().wInfo('开始读取配置文件')
        return self.obj_config.get(str_section, str_option)

    def setConfigData(self, str_section, str_option, str_content):
        """
        设置conf文件value值操作
        :param str_section:
        :param str_option:   conf文件section的名称 [ XXX ]
        :param str_content:  conf文件option的名称（key）
        :return: 是否写入成功
        """
        bol_isWrite = True
        try:
            self.obj_config.set(str_section,str_option,str_content)
            self.obj_config.write(open(self.str_confFileName, 'w'))
        except Exception as e:
            bol_isWrite = False
            print('错误：',e)

        return bol_isWrite

if __name__ == '__main__':
    print(UtilConfig(sys.path[0] + '/config/' + 'smtpconf.conf').getConfigData('STMPMASSAGEMIAL','config'))



