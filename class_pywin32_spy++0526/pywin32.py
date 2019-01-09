# -*- coding: utf-8 -*-
# @Time    : 2018/5/27 18:24
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : pywin32.py
# @Software: PyCharm


import win32gui
import win32con


#找到窗口  一层一层往下找
dialog = win32gui.FindWindow('#32770','打开')#一级窗口
ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)#二级窗口
comboBox = win32gui.FindWindowEx(ComboBoxEx32,0,"ComboBox",None) #三级
edit = win32gui.FindWindowEx(comboBox,0,'Edit',None)#四级

button = win32gui.FindWindowEx(dialog,0,"Button","打开(&O)")#四级
file_path='D:\\build.txt'#文件名

#操作
win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,file_path)#发送文件路径

win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)#点击打开按钮























