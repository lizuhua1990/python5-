# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 22:00
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : test_login.py
# @Software: PyCharm

import unittest
from selenium import webdriver
from class_WEB_Framework_v20607.PageObjects.login_Page import LoginPage
from class_WEB_Framework_v20607.PageObjects.home_page import HomePage
from class_WEB_Framework_v20607.TestDatas.login_testdata import *
from class_WEB_Framework_v20607.TestDatas.Common_Data import *
import pytest
#pytest-运行方法：
#搜索目录下的标记表达式来执行：pytest -m smoke
#1、指定模块名： pytest TestCases/test_login.py
#2、指定目录下：pytest TestCases/\
#3、进入目录：cd TestCases  执行：pytest test_login.py::Test_Login::test_login_noPasswd
#4、添加报告生成：pytest --html TestReport/report.html TestCases/test_login.py::Test_Login::test_login_noPasswd
#5、执行某个文件中带标签的用例生成报告：pytest -m smoke --html TestReport/report.html --junitxml TestReport/report.xml TestCases/test_login.py

@pytest.mark.login
class Test_Login(unittest.TestCase):

    def setUp(self):
        print('web自动化测试开始咯！')
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        #self.verificationErrors=[]
        pass

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print('web自动化测试结束了！')

    # 没有密码的时候
    # 在测试用例、测试类前面加上：@pytest.mark.标记名
    @pytest.mark.smoke
    # 可以多个标签组合使用，在符合这两个标签的时候运行
    @pytest.mark.Test
    def test_login_noPasswd(self):
        #引入测试数据
        #执行步骤
        lp=LoginPage(self.driver)
        lp.login(url,user_name,login_data[1]['passwd'])
        #期望结果和实际结果的对比
        self.assertEqual(lp.get_errorMsg_from_loginArea(),login_data[1]['check_msg'])

    #正常登录的时候
    @pytest.mark.Test
    def test_login_ok(self):
        #引入测试数据
        #执行步骤
        lp=LoginPage(self.driver)
        lp.login(url,login_data[0]['user_name'],login_data[0]['passwd'])
        #期望结果和实际结果的对比
        hp=HomePage(self.driver)
        nicknam=hp.get_user_nickname()
        self.assertEqual(nicknam, login_data[0]['check_msg'])
        #可以尝试另一种方法处理
        # try:
        #     hp.get_nickname_ele(login_data[0]['check_msg'])
        # except Exception as e:
        #     self.verificationErrors.append(e)
        # self.assertEqual([],self.verificationErrors)




