#!/usr/bin/python
#coding=utf-8
'''
Created on 2017/4/1

@author: luxk

注释：
正则表通常被用来检索、替换那些符合某个模式(规则)的文本。
'''

import re

class mytest():
	def func1(self):
		str1 = "hello word!"
		str2 = "hello"

		print(str1.find('e'))
		print(str1.split('e'))
		print(str1.replace('e','a'))

		#判断str1中是否包含str2字符
		if str2 in str1:
			print("存在包含关系..")


	def findall_01(self):
		str1 = "hello word!"
		str2 = "o"
		#匹配字符串
		print(re.findall(str2,str1))





	def func2(self):
		print(re.compile("ahello").match('hello word!').group())

	#compile 用法
	def func3(self):
		# 定义一个正则模板对象
		#字符串
		str_comp = 'helooHELLOhellohellohellohellohello'
		#元字符
		"""
		.	匹配除换行符以外的任意一个字符
		^	匹配行首
		$	匹配行尾
		？	重复匹配0次或1次
		*	重复匹配0次或更多次
		+	重复匹配1次或更多次
		{n,}	重复n次或更多次
		{n,m}	重复n~m次
		[a-z]	任意一个字符
		[abc]	a/b/c中的任意一个字符 除了^ - 和\以外其余元字符在[]均作为普通字符处理
		{n}	重复n次
		\ :反斜线后面跟元字符去除特殊功能，跟普通字符实现特殊功能；后面跟数字表示第几个组
		\d 匹配一个数字字符。等价于[0 - 9]
		\D 匹配一个非数字字符。等价于[^0-9]
		\s 匹配任何不可见字符，包括空格、制表符、换页符等等。等价于[ \f\n\r\t\v]
		\S 匹配任何可见字符。等价于[^ \f\n\r\t\v]
		\w 匹配包括下划线的任何单词字符。类似于“[A-Za-z0-9_]”
		\W 匹配任何非单词字符。等价于“[^A-Za-z0-9_]”
		\b 匹配一个单词边界，也就是指单词和空格间的位置
		"""
		#'hellohelooHELLO'
		# comp2 = re.compile(".ello")

		# comp2 = re.compile("^hello")
		# comp2 = re.compile("hello$",re.I)
		# comp2 = re.compile("hello?")
		# comp2 = re.compile("hello*")
		# comp2 = re.compile("hello+")
		# comp2 = re.compile("hello{1,}")
		# comp2 = re.compile("hello{1,3}")
		# comp2 = re.compile("he[a-z]lo")
		# comp2 = re.compile("he[l]lo")
		# comp2 = re.compile("hel{1}o")

		#其它用法
		comp2 = re.compile("hel[l|o]o")
		comp2 = re.compile("h+?e")
		# comp2 = re.compile("hel[^l]o")
		# comp2 = re.compile('HELLO', re.I)

		# print(comp2.search(str_comp).group())

		#反斜线组的用法
		# print(re.search(r"a","aaaaabbccddeedd").group())
		# print(re.match(r"a","aaaaabbccddeedd"))
		# print(re.findall(r"a","aaaaabbccddeedd"))

		#非贪婪模式 ？ 若?后面跟着匹配字符，则无效
		# print(re.search("a(b+?)","aaaabbbcccc").group())
		# print(re.search("a(b+?)c","aaaabbbcccc").group())


		#替换
		print(re.sub('\d','s','11a23b34c34d'))

		#分隔
		print(re.split('\d','a1b2c3d'))


if __name__ == '__main__':
    # mytest().func1()
    # mytest().findall_01()
    # mytest().func2()
    mytest().func3()