# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 22:16
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : main_all.py
# @Software: PyCharm


import pytest

pytest.main(['--html=TestReport/allCase_report.html','--junitxml=TestReport/allCasereport.xml','TestCases'])
