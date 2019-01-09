# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 9:16
# @Author  :
# @Email   :
# @File    : config.py
# @Software: PyCharm

import os
import configparser

class config:
    def read_config(self,conf_path,section,option):
        rc=configparser.RawConfigParser()
        rc.read(conf_path,encoding='utf-8')
        result=eval(rc.get(section,option))
        return result

if __name__ == '__main__':
    print(config ().read_config (os.path.dirname (os.getcwd ()) + '/conf/' + 'db.conf', 'DBCONFIG', 'config'))