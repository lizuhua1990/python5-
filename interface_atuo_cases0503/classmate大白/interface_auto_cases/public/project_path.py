import os
project_path=os.path.split(os.path.realpath(__file__))[0] #获取project模块的路径
#print(project_path)

httprequestconfig_path=os.path.join(os.path.split(project_path)[0],"config","http_request.conf")#获取配置文件的路径
#print(httprequestconfig_path)

excle_path=os.path.join(os.path.split(project_path)[0],"test_data","interfaceCases_data.xlsx")#获取excel文件路径
#print(excle_path)