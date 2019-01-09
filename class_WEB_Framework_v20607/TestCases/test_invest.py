# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 16:33
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : test_invest.py
# @Software: PyCharm

import unittest
from selenium import webdriver
from class_WEB_Framework_v20607.PageObjects.login_Page import LoginPage
from class_WEB_Framework_v20607.PageObjects.home_page import HomePage
from class_WEB_Framework_v20607.PageObjects.loan_page import LoanPage
from class_WEB_Framework_v20607.TestDatas.Common_Data import *
from class_WEB_Framework_v20607.TestDatas.invest_testdata import *
from class_WEB_Framework_v20607.PageLocators.loan_page_locators import Loan_Locator as LL
from class_WEB_Framework_v20607.PageObjects.userinfo_page import UserInfoPage
import time
import pytest

# 前提：不在继承使用unittest.TestCase，完全使用pytest
# 前提：在conftest.py中定义一个fixture，对应的函数名为init_driver
# 第一步：先使用@pytest.mark.usefixtures('init_driver')，将对应的fixture引入
# 第二步：将init_driver作为测试用例的参数
# 第三步：如果fixture是有返回值的，那么在测试用例中，调用的时候，直接是fixture的函数名称接受返回值的。
# 第四步：不在使用unittest的断言，使用assert ,表他说的方式来断言

# fixture的参数中，有scope作用域：
# 1、function:每个test都运行，默认是function的scope，即unittest中的Setup和tearDown
# 2、class：每个class的所有test只运行一次，即unittest中的SetupClass和tearDownClass
# 3、module：每个module的所有test只运行一次
# 4、session：每个session只运行一次
@pytest.mark.usefixtures('init_driver')#运行定义的函数，返回该函数的返回值
class Test_Invest():

    # def setUp(self):
    #     print('web自动化测试开始咯！')
    #     init_driver=webdriver.Chrome()
    #     init_driver.maximize_window()
    #     pass
    #
    # def tearDown(self):
    #     init_driver.close()
    #     init_driver.quit()
    #     print('web自动化测试结束了！')

    # 投资成功
    @pytest.mark.smoke
    def test_invest_ok (self,init_driver):
        # 引入测试数据
        # 执行步骤
        # lp = LoginPage(init_driver)
        # lp.login(url, invest_ok_testData['user_name'], invest_ok_testData['passwd'])
        hp = HomePage(init_driver)
        hp.click_InvestButton()
        #time.sleep(20)
        # 获取投标名称
        investname = LoanPage(init_driver).get_Investname()
        # 获取余额
        LeftMoney = LoanPage(init_driver).get_userLeftMoney()
        # 进行投标
        Invest_msg = LoanPage(init_driver).put_Investmoney(invest_ok_testData['money'], LL.ok_link_xpath)
        # 点击进入个人页面
        LoanPage(init_driver).click_popup_activeButton()
        # 获取投资后余额
        get_leftmoney = str(
            float(UserInfoPage(init_driver).get_userLeftMoney()) + float(invest_ok_testData['money']))
        # 点击投资Tab 展开投资记录
        UserInfoPage(init_driver).click_investRecord_tab()
        # 查看获取记录的标名
        get_investname = UserInfoPage(init_driver).get_firstLoanName_byInvestRecord()

        # 期望结果和实际结果的对比
        assert LeftMoney == get_leftmoney
        assert invest_ok_testData['check_msg'] in Invest_msg
        assert investname in get_investname

    # 投资失败
    def test_invest_no (self,init_driver):
        # 引入测试数据
        # 执行步骤
        # lp = LoginPage(init_driver)
        # lp.login(url, invest_no_testData['user_name'], invest_no_testData['passwd'])
        hp = HomePage(init_driver)
        hp.click_InvestButton()
        # 获取投标名称
        investname = LoanPage(init_driver).get_Investname()
        # 进行投标
        Invest_msg = LoanPage(init_driver).put_Investmoney(invest_no_testData['money'], LL.error_link_xpath)
        # 期望结果和实际结果的对比
        self.assertEqual(Invest_msg, invest_no_testData['check_msg'])
