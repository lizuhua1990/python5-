#Author:Xiao Jian

import win32gui
import win32con

#控件查找 - 一层一层往下找
dialog = win32gui.FindWindow("#32770","打开")
ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)
comboBox = win32gui.FindWindowEx(ComboBoxEx32,0,"ComboBox",None)   #三级
edit = win32gui.FindWindowEx(comboBox,0,'Edit',None)

button = win32gui.FindWindowEx(dialog,0,"Button","打开(&O)")

file_path = "D:\\build.txt"

#操作
win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,file_path)    #发送文件路径
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)    #点击打开按钮



