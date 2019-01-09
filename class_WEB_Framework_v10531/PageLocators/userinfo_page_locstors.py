# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 12:08
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : userinfo_page_locstors.py
# @Software: PyCharm


class UserInfo_page:

    #个人可用余额元素
    user_leftMoney_xpath='//*[@class="personal_info"]//li[@class="color_sub"]'

    #投资项目元素定位
    click_InvestRecords_tab_xpath='//div[text()="投资项目"]'

    #个人详情页--第一条投资记录
    first_investRecord_xpath='//table[@class="deal_mange_tab"]//tr'

    #投资记录中，标名对应的属性值
    investRecord_loanName='//*[@ms-html="item.title"]/a'








