# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 20:28
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : loan_page.py
# @Software: PyCharm0

from class_WEB_Framework_v20607.PageLocators.loan_page_locators import Loan_Locator as LL
import time
from class_WEB_Framework_v20607.PageObjects.BasePage import BasePage


class LoanPage(BasePage):

    #获取投资的名称
    def get_Investname(self):
        # 等待页面元素出现
        return self.get_element(LL.invest_name_xpath).text

    #进行金额投资输入点击
    def put_Investmoney(self,money,link_xpath):
        # 先找到这个元素，然后拖动到可见区域
        target = self.driver.find_element_by_xpath(LL.invest_name_xpath)
        # 利用js。拖动到可见的元素去
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        #定位输入框，输入金额
        self.get_element(LL.invest_money_xpath).send_keys(money)
        time.sleep(1)
        #点击投标按钮
        self.get_element(LL.invest_moneybutton_xpath).click()
        #获取返回信息
        invest_msg=self.get_element(link_xpath).text
        #点击进入个人页面
        #self.driver.find_element_by_xpath(LL.invest_failed_popup_xpath).click()
        return invest_msg

    #获取个人余额
    def get_userLeftMoney(self):
        #等待元素出现
        #获取金额输入框的data-amount属性值
        return self.get_element(LL.userLeftMoney_xpath).get_attribute('data-amount')

    #点击查看并激活——跳转到个人页面
    def click_popup_activeButton(self):
        # 等待元素出现
        #点击
        self.get_element(LL.invest_failed_popup_xpath).click()






