# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 23:30
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : home_page.py
# @Software: PyCharm

from class_WEB_Framework_v20607.PageLocators.home_page_locators import Home_Loceator as HL
import time
from class_WEB_Framework_v20607.PageObjects.BasePage import BasePage


class HomePage(BasePage):

    def get_user_nickname(self):
        #等待页面元素出现
        self.wait_eleVisible(HL.userinfo_link_xpath)
        return self.driver.find_element_by_xpath(HL.userinfo_link_xpath).text

    #随机选择一个标,点击其抢投标按钮，进入标的详情页面
    def click_InvestButton(self):
        # 等待页面元素出现
        #找到首页的标
        #eles=self.driver.find_element_by_xpath(HL.invest_button_xpath)
        #print(eles)
        #index=random.randint(eles)
        # 有滚动的页面-需要看路滚动条处理，因为使用者的功能调用顺序很随机
        # 先找到这个元素，然后拖动到可见区域
        self.wait_eleVisible(HL.invest_button_xpath)
        self.scroll_element_intoView(HL.invest_button_xpath)
        time.sleep(1)
        #点击随机指定的抢投标按钮
        self.get_element(HL.invest_button_xpath).click()

    def get_nickname_ele(self,nickname_text):
        #等待页面元素出现
        self.get_element(HL.userinfo_link_xpath % nickname_text)





