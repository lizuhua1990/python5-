# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 12:11
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : userinfo_page.py
# @Software: PyCharm

from class_WEB_Framework_v20607.PageLocators.userinfo_page_locstors import UserInfo_page as UI
import time
from class_WEB_Framework_v20607.PageObjects.BasePage import BasePage

class UserInfoPage(BasePage):

    #获取用户余额
    def get_userLeftMoney(self):
        self.wait_eleVisible(UI.user_leftMoney_xpath)
        self.scroll_element_intoView(UI.user_leftMoney_xpath)
        #获取money
        money=self.get_element(UI.user_leftMoney_xpath).text
        #截取数字部分
        money= money.split('元')
        return money[0]

    #点击投资Tab 展开投资记录
    def click_investRecord_tab(self):
        self.wait_eleVisible(UI.click_InvestRecords_tab_xpath)
        self.scroll_element_intoView(UI.click_InvestRecords_tab_xpath)
        self.get_element(UI.click_InvestRecords_tab_xpath).click()
        time.sleep(0.5)

    #获取第一条投资记录的标名
    def get_firstLoanName_byInvestRecord(self):
        #等待元素出现
        self.wait_eleVisible(UI.first_investRecord_xpath)
        self.scroll_element_intoView(UI.first_investRecord_xpath)
        #获取对应的标名
        loanName=self.get_element(UI.first_investRecord_xpath+UI.investRecord_loanName).text
        return loanName










