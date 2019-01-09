__author__ = '20489'
import  configparser

class readConfig:
    def get_value(self,filepath,section,option):
        cf=configparser.ConfigParser()
        cf.read(filepath)
        value=cf.get(section,option)
        return value