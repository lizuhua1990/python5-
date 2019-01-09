# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 23:30
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : home_page.py
# @Software: PyCharm

from class_WEB_Framework_v10531.PageLocators.home_page_locators import Home_Loceator as HL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class HomePage:
    def __init__(self,driver):
        # 初始化
        self.driver=driver

    def get_user_nickname(self):
        #等待页面元素出现
        WebDriverWait(self.driver,15,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,HL.userinfo_link_xpath)))
        return self.driver.find_element_by_xpath(HL.userinfo_link_xpath).text

    #随机选择一个标,点击其抢投标按钮，进入标的详情页面
    def click_InvestButton(self):
        # 等待页面元素出现
        WebDriverWait(self.driver, 15, 0.5).until(EC.visibility_of_element_located((By.XPATH, HL.invest_button_xpath)))
        #找到首页的标
        #eles=self.driver.find_element_by_xpath(HL.invest_button_xpath)
        #print(eles)
        #index=random.randint(eles)
        # 有滚动的页面-需要看路滚动条处理，英文使用者的功能调用很随机
        # 先找到这个元素，然后拖动到可见区域
        target = self.driver.find_element_by_xpath(HL.invest_button_xpath)
        # 利用js。拖动到可见的元素去
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(1)
        #点击随机指定的抢投标按钮
        self.driver.find_element_by_xpath(HL.invest_button_xpath).click()






