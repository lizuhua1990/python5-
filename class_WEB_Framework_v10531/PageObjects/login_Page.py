# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 21:38
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : login_Page.py
# @Software: PyCharm

import time

class LoginPage:

    def __init__(self,driver):
        # 初始化
        self.driver=driver

    #实现登录功能，页面元素定位、页面的功能登录
    #元素定位
    login_username_xpath="//*[@name='phone']"
    login_passwd_xpath="//*[@name='password']"
    login_button_xpath="//button"

    #登录区域--错误提示信息
    prompt_from_loginArea_xpath="//*[@class='form-error-info']"

    def login(self,url,username,passed):
        self.driver.get(url)
        self.driver.find_element_by_xpath(self.login_username_xpath).send_keys(username)
        self.driver.find_element_by_xpath(self.login_passwd_xpath).send_keys(passed)
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
        #不需要做判断处理-数据结果不同，在用例断言是判断

    # 获取登录区域的错误提示信息
    def get_errorMsg_from_loginArea (self):
        time.sleep(1)
        return self.driver.find_element_by_xpath(self.prompt_from_loginArea_xpath).text