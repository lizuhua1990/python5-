# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 23:31
# @Author  :
# @Email   :
# @File    : home_page_locators.py
# @Software: PyCharm


class Home_Loceator:
    #登录后首页昵称文本信息路径
    userinfo_link_xpath='//a[@href="/Member/index.html"]'

    #投标按钮元素路径
    invest_button_xpath='//span[text()=" python自动化项目"]/ancestor::a/following-sibling::div//a'

