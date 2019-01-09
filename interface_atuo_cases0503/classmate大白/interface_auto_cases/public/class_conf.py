import configparser

class readConfig:
    def readConf(self,path,section, option,):
        cf=configparser.RawConfigParser()
        cf.read(path,encoding="utf-8")
        cf_data=cf.get(section, option,)
        return cf_data

if __name__=="__main__":

    r=readConfig().readConf("G:\interfaceTest\interface_auto_cases\config\http_request.conf","IP","ip")
    print(eval(r))