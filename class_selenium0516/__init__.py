# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 20:53
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : __init__.py.py
# @Software: PyCharm

from wxpy import *

#bot=Bot()
bot=Bot(cache_path=True)#登录微信


'''给自己发送“我爱你“'''
# 在Web微信中把自己加为好友
bot.self.add()
bot.self.accept()
# 发送消息给自己
bot.self.send(" 520，我爱你!")

'''指定聊天对象，大胆进行表白吧
#指定聊天对象，并发送你想说的话#还可以发送图片，视频，文件或者动图等。可以试一下
my_friend = bot.friends().search('金山角')[0]
found = ensure_one(my_friend) #确保找到的是唯一，避免重复
my_friend.send("在干嘛呢（来自程序自动发送！）")
#如何指定聊天回复你了，聊天机器人自动回复设置好的消息。
@bot.register(my_friend)
def reply_my_friend(msg):
    return '{} ，收到你的消息了'.format(msg.text, msg.type)
#指定聊天对象，聊天机器人拒绝回复他的消息
ignore_friend = bot.friends().search('金山角')[0]
@bot.register(ignore_friend)
def ignore(msg):
    return'''

'''指定一个群聊，并且自动回复群里的消息'''
boring_group = bot.groups().search('金山角')[0]
@bot.register(boring_group)
def reply_my_friend(msg):
    return '{} ，收到你的消息了,马上处理'.format(msg.text, msg.type)
#忽略群里的消息
@bot.register(boring_group)
#忽略群的消息
def ignore(msg):
#什么也不做
    return


