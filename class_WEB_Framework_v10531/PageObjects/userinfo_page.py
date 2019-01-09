# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 12:11
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : userinfo_page.py
# @Software: PyCharm

from class_WEB_Framework_v10531.PageLocators.userinfo_page_locstors import UserInfo_page as UI
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class UserInfoPage:
    def __init__(self,driver):
        # 初始化
        self.driver=driver


    #获取用户余额
    def get_userLeftMoney(self):
        #等待元素可见
        WebDriverWait(self.driver,15,0.5).until(EC.visibility_of_element_located((By.XPATH,UI.user_leftMoney_xpath)))
        # 先找到这个元素，然后拖动到可见区域
        target = self.driver.find_element_by_xpath(UI.user_leftMoney_xpath)
        # 利用js。拖动到可见的元素去
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        #获取money
        money=self.driver.find_element_by_xpath(UI.user_leftMoney_xpath).text
        #截取数字部分
        money= money.split('元')
        return money[0]

    #点击投资Tab 展开投资记录
    def click_investRecord_tab(self):
        #等待元素出现
        WebDriverWait(self.driver,15,0.5).until(EC.visibility_of_element_located((By.XPATH,UI.click_InvestRecords_tab_xpath)))
        # 先找到这个元素，然后拖动到可见区域
        target = self.driver.find_element_by_xpath(UI.click_InvestRecords_tab_xpath)
        # 利用js。拖动到可见的元素去
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        target.click()
        time.sleep(0.5)

    #获取第一条投资记录的标名
    def get_firstLoanName_byInvestRecord(self):
        #等待元素出现
        WebDriverWait(self.driver,15,0.5).until(EC.visibility_of_element_located((By.XPATH,UI.first_investRecord_xpath)))
        # 先找到这个元素，然后拖动到可见区域
        target = self.driver.find_element_by_xpath(UI.first_investRecord_xpath)
        # 利用js。拖动到可见的元素去
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        #获取对应的标名
        loanName=self.driver.find_element_by_xpath(UI.first_investRecord_xpath+UI.investRecord_loanName).text
        return loanName










