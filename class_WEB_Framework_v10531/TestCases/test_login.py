# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 22:00
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : test_login.py
# @Software: PyCharm

import unittest
from selenium import webdriver
from class_WEB_Framework_v10531.PageObjects.login_Page import LoginPage
from class_WEB_Framework_v10531.PageObjects.home_page import HomePage
from class_WEB_Framework_v10531.PageObjects.loan_page import LoanPage
from class_WEB_Framework_v10531.TestDatas.login_testdata import *
from class_WEB_Framework_v10531.PageLocators.loan_page_locators import Loan_Locator as LL
from class_WEB_Framework_v10531.PageObjects.userinfo_page import UserInfoPage


class Test_Login(unittest.TestCase):

    def setUp(self):
        print('web自动化测试开始咯！')
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        pass

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print('web自动化测试结束了！')

    #没有密码的时候
    def test_login_noPasswd(self):
        #引入测试数据
        #执行步骤
        lp=LoginPage(self.driver)
        lp.login(url,login_data[1]['user_name'],login_data[1]['passwd'])
        #期望结果和实际结果的对比
        self.assertEqual(lp.get_errorMsg_from_loginArea(),login_data[1]['check_msg'])

    #正常登录的时候
    def test_login_ok(self):
        #引入测试数据
        #执行步骤
        lp=LoginPage(self.driver)
        lp.login(url,login_data[0]['user_name'],login_data[0]['passwd'])
        #期望结果和实际结果的对比
        hp=HomePage(self.driver)
        nicknam=hp.get_user_nickname()
        self.assertEqual(nicknam, login_data[0]['check_msg'])


    #投资成功
    def test_invest_ok(self):
        #引入测试数据
        #执行步骤
        lp=LoginPage(self.driver)
        lp.login(url,invest_ok_testData['user_name'],invest_ok_testData['passwd'])
        hp=HomePage(self.driver)
        hp.click_InvestButton()
        #获取投标名称
        investname =LoanPage(self.driver).get_Investname()
        #获取余额
        LeftMoney=LoanPage(self.driver).get_userLeftMoney()
        #进行投标
        Invest_msg=LoanPage(self.driver).put_Investmoney(invest_ok_testData['money'],LL.ok_link_xpath)
        #点击进入个人页面
        LoanPage(self.driver).click_popup_activeButton()
        #获取投资后余额
        get_leftmoney=str(float(UserInfoPage(self.driver).get_userLeftMoney())+ float(invest_ok_testData['money']))
        # 点击投资Tab 展开投资记录
        UserInfoPage(self.driver).click_investRecord_tab()
        #查看获取记录的标名
        get_investname= UserInfoPage(self.driver).get_firstLoanName_byInvestRecord()

        #期望结果和实际结果的对比
        self.assertEqual(LeftMoney,get_leftmoney)
        self.assertEqual(Invest_msg,invest_ok_testData['check_msg'])
        self.assertEqual(investname,get_investname)


    #投资失败
    def test_invest_no(self):
        #引入测试数据
        #执行步骤
        lp=LoginPage(self.driver)
        lp.login(url,invest_no_testData['user_name'],invest_no_testData['passwd'])
        hp=HomePage(self.driver)
        hp.click_InvestButton()
        #获取投标名称
        investname =LoanPage(self.driver).get_Investname()
        #进行投标
        Invest_msg=LoanPage(self.driver).put_Investmoney(invest_no_testData['money'],LL.error_link_xpath)
        #期望结果和实际结果的对比
        self.assertEqual(Invest_msg,invest_no_testData['check_msg'])






'''2. 用fixture装饰器调用fixture：
   在测试用例/测试类前面加上@pytest.mark.usefixtures(“fixture函数名字”)
    ps: 定义conftest.py文件，在此文件中可定义多个fixture.pytest会自动搜索此文件。'''




