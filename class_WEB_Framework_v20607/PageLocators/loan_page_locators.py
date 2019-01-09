# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 20:48
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : loan_page_locators.py
# @Software: PyCharm

class Loan_Locator:
    #投资的名称定位
    invest_name_xpath='//div[@class="float_left"]'
    # 输入框元素定位路径
    invest_money_xpath = '//input[@data-id="5765"]'
    # 投标按钮元素定位路径
    invest_moneybutton_xpath = '//button[@class="btn btn-special height_style"]'
    #错误提示元素定位
    error_link_xpath='//div[@id="layui-layer1"]//div[@class="text-center"]'
    #投标成功元素定位
    ok_link_xpath='//div[@id="layui-layer1"]//div[@class="capital_font1 note"]'
    #可用余额元素定位
    userLeftMoney_xpath='//input[@data-id="5765"]'
    #投资成功弹出框 查看并激活按钮元素定位
    invest_failed_popup_xpath='//div[@id="layui-layer1"]//button[text()="查看并激活"]'





