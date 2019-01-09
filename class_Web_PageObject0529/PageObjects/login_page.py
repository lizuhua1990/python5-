# -*- coding: utf-8 -*-
# @Time    : 2018/5/30 10:27
# @Author  :
# @Email   :
# @File    : login_page.py
# @Software: PyCharm


from selenium import webdriver
import time

class LoginPage:

    def __init__(self,driver):
        # 初始化
        #self.driver=webdriver.Chrome()
        #self.driver.maximize_window()
        self.driver=driver
        #get网址

    #实现登录功能，页面元素定位、页面的功能登录
    #元素定位
    login_username_xpath="//*[@name='phone']"
    login_passwd_xpath="//*[@name='password']"
    login_button_xpath="//button"

    #登录区域--错误提示信息
    prompt_from_loginArea_xpath="//*[@class='form-error-info']"

    #登录后首页文本信息路径
    text_from_sy_xpath='//div[@class="center position"]//a[text()="首页"]'


    def login(self,url,username,passed):
        self.driver.get(url)
        self.driver.find_element_by_xpath(self.login_username_xpath).send_keys(username)
        self.driver.find_element_by_xpath(self.login_passwd_xpath).send_keys(passed)
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
        #不需要做判断处理-数据结果不同，在用例断言是判断

    #获取登录区域的错误提示信息
    def get_errorMsg_from_loginArea(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath(self.prompt_from_loginArea_xpath).text


    #获取登录跳转页面首页文本信息
    def get_msg_from_text(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath(self.text_from_sy_xpath).text















