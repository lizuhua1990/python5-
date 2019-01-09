# -*- coding: utf-8 -*-
# @Time    : 2018/5/30 11:32
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : login_page_locators.py
# @Software: PyCharm


class Login_Loceator:
    # 元素定位
    login_username_xpath = '//*[@name="phone"]'
    login_passwd_xpath = '//*[@name="passwd"]'
    login_button_xpath = '//button'

    # 登录区域--错误提示信息
    prompt_from_loginArea_xpath = '//*[@class="from-error-info"]'
