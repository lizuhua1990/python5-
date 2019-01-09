# -*- coding: utf-8 -*-
# @Time    : 2018/5/30 10:53
# @Author  :
# @Email   :
# @File    : test_login.py
# @Software: PyCharm


'''
作业：PO模式应用

完成上课老师写的代码部分。
另外，你们再补充-登陆成功的用例
'''

import unittest
from selenium import webdriver
from class_Web_PageObject0529.PageObjects.login_page import LoginPage

class Test_Login(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        print('web自动化测试开始咯！')


    #登录的时候 -密码没有
    def test_login_noPasswd(self):
        #测试数据
        url="http://120.78.128.25:8765/Index/login.html"
        user_name='13760246701'
        passwd=''
        check_msg="请输入密码"
        #执行步骤
        lp=LoginPage(self.driver)
        lp.login(url,user_name,passwd)
        #期望结果和实际结果的对比
        self.assertEqual(lp.get_errorMsg_from_loginArea(),check_msg)

    #正常登录的时候
    def test_login_ok(self):
        #测试数据
        url="http://120.78.128.25:8765/Index/login.html"
        user_name='13760246701'
        passwd='python_test'
        check_msg="首页"
        #执行步骤
        lp=LoginPage(self.driver)
        lp.login(url,user_name,passwd)
        #期望结果和实际结果的对比
        self.assertEqual(lp.get_msg_from_text(), check_msg)

    def tearDown(self):
        print('web自动化测试结束了！')


if __name__ == '__main__':
    suite=unittest.TestSuite()#实例
    suite.addTest(Test_Login('test_login_ok'))