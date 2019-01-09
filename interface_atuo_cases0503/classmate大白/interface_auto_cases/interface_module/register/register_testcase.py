import requests
from public import project_path
from public.class_conf import readConfig
from public.excel_rw import excel_rw

config=readConfig()#创建config读取实例
rw=excel_rw(project_path.excle_path, "register")  # 创建读写register实例
read_data=rw.readInfo()  # 调用读方法读取测试数据
print("读取数据为：", read_data)
init=excel_rw(project_path.excle_path, "init")  # 创建init数据实例
# 建立请求地址
ip=config.readConf(project_path.httprequestconfig_path, "IP", "ip")  # 从配置文件取ip
url=eval(ip) + "/futureloan/mvc/api/member/register"  # 拼接地址
print("url=", url)
mode=config.readConf(project_path.httprequestconfig_path,"FLAG","mode")
print("mode =",mode)
case_list=config.readConf(project_path.httprequestconfig_path,"FLAG","case_list")
print("case_list =",case_list)

#遍历读取的测试数据，完成请求
for i in range(len(read_data)):
    if eval(mode)==0:
        data = {}  # 初始化测试数据字典
        if read_data[i]["Mobilephone"]=="$mobilephone":
            init_data = init.readInfo()  # 读init表单数据
            #添加data请求参数数据
            data["mobilephone"]=init_data[0]["$mobilephone"]+1
            data["pwd"]=read_data[i]["Pwd"]
            data["regname"]=read_data[i]["Regname"]
            print("请求data为：",data)
            result=requests.get(url,data).json() #返回测试结果

            #更新init数据
            updata=init_data[0]["$mobilephone"]+1
            init.witeInfo(2,1,updata)
            print("mobilephone更新为：",init_data[0]["$mobilephone"]+1)
        else:
            data["mobilephone"] = read_data[i]["Mobilephone"]
            data["pwd"] = read_data[i]["Pwd"]
            data["regname"] = read_data[i]["Regname"]
            print(data)
            result = requests.get(url, data).json()  # 返回测试结果
        # 将测试结果写入excle Actual-code
        rw.witeInfo(i + 2, 7, result["code"])
        print("写入测试结果：", result["code"])

        # 判断预期结果和实际结果是否一致 写入Result
        if read_data[i]["Expected_code"] == int(result["code"]):
            rw.witeInfo(i + 2, 8, "pass")
            print("预期结果：", read_data[i]["Expected_code"], "实际结果", int(result["code"]), "写入:pass")
        else:
            rw.witeInfo(i + 2, 8, "fail")
            print("预期结果：", read_data[i]["Expected_code"], "实际结果", int(result["code"]), "写入:fail")

        # 写入msg，Reason
        rw.witeInfo(i + 2, 9, result["msg"])
        print("msg:", result["msg"])
    else:
        if read_data[i]["Id"] in eval(case_list):
            print("Id=", read_data[i]["Id"])
            data = {}  # 初始化测试数据字典
            if read_data[i]["Mobilephone"] == "$mobilephone":
                init_data = init.readInfo()  # 读init表单数据
                # 添加data请求参数数据
                data["mobilephone"] = init_data[0]["$mobilephone"] + 1
                data["pwd"] = read_data[i]["Pwd"]
                data["regname"] = read_data[i]["Regname"]
                print(data)
                result = requests.get(url, data).json()  # 返回测试结果

                # 更新init数据
                updata = init_data[0]["$mobilephone"] + 1
                init.witeInfo(2, 1, updata)
                print("mobilephone更新为：", init_data[0]["$mobilephone"] + 1)
            else:
                data["mobilephone"] = read_data[i]["Mobilephone"]
                data["pwd"] = read_data[i]["Pwd"]
                data["regname"] = read_data[i]["Regname"]
                print(data)
                result = requests.get(url, data).json()  # 返回测试结果

            # 将测试结果写入excle Actual-code
            rw.witeInfo(i + 2, 7, result["code"])
            print("写入测试结果：", result["code"])

            # 判断预期结果和实际结果是否一致 写入Result
            if read_data[i]["Expected_code"] == int(result["code"]):
                rw.witeInfo(i + 2, 8, "pass")
                print("预期结果：", read_data[i]["Expected_code"], "实际结果", int(result["code"]), "写入:pass")
            else:
                rw.witeInfo(i + 2, 8, "fail")
                print("预期结果：", read_data[i]["Expected_code"], "实际结果", int(result["code"]), "写入:fail")

            # 写入msg，Reason
            rw.witeInfo(i + 2, 9, result["msg"])
            print("msg:", result["msg"])

