# -*- coding: utf-8 -*-
# @Time    : 2018/6/22 21:24
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : __init__.py.py
# @Software: PyCharm

'''
4.1 与Appium服务器相关的

Capability	是否为必填项	描述	值
automationName	否	Appium使用的测试引擎	Appium（默认）
platformName	是	被测设备的系统平台	iOS，Android，Firefox OS，null（默认）
platformVersion	否	手机系统版本	如6.6.1,null（默认）
deviceName	否	测试设备类型（测试Android时被忽略）	null（默认）
app	否	指向APP安装文件，Android中如果设置了appActivity和appPackage，则此会被忽略	null（默认）
browserName	否	手机网页测试时浏览器的名称	设置为Safari在测iOS和Chrome时,设置为Browser在测Android时
newCommandTimeout	否	Appium服务器等待Appium客户端发送新消息的时间，单位为s	60s（默认）
language	否	（仅模拟器使用）设置模拟器的语言	null（默认）
locale	否	（仅模拟器使用）设置模拟器的使用国家	null（默认）
udid	否	（仅真机使用）测试设备的ID	在多台设备与同一台电脑连接时必须指定
orientation	否	（仅模拟器使用）屏幕方向	LANDSCAPE，PORTRAIT，null（默认）
autoWebview	否	直接切换到WebView上下文	false（默认），true
noReset	否	在一个Session开始前不重置被测程序的状态	false（默认），true
fullReset	否	完全重置（Android通过卸载程序的方式），Session完成后会卸载程序	false（默认），true

4.2 仅对Android测试有效的设置

Capability	是否为必填项	描述	值
appActivity	是	被测APP启动的Activity名称	如.MainActivity
appPackage	是	被测APP的包名	例如：com.example.android.myApp
deviceReadyTimeout	否	等待设备ready的超时时间	5s（默认）
ignoreUnimportantViews	否	会忽略一些控件，加快运行	false（默认），true
disableAndroidWatchers	否	只针对基于UIAutomator的测试有效，不会监控ANR和Crash，这将较少CPU消耗	false（默认），true
unicodeKeyboard	否	是否支持Unicode的键盘，如果输入中文，设置为是	false（默认），true
resetKeyboard	否	测试结束后是否恢复键盘，为正常的手机键盘	false（默认），true
androidScreenshotPath	否	截图存放的目录	/data/local/tmp（默认）





'''