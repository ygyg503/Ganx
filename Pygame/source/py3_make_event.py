#!/usr/bin/python
#-*-coding:utf-8-*-
import pygame
from pygame.locals import *
#当除去上面这行，会提示KEYDOWN没有定义
#pygame.locals存放的是 pygame constants Py常量

pygame.init()
#处理可以定义locals constants以外，原来还可以自定义全新事件阿

CATONKEYBOARD = USEREVENT + 1
#CATONKEYBOARD 化成小写 catonkeyboard...阿猫阿狗啥的应该算自定义把
#USEREVENT是定好的常量了
my_event = pygame.event.Event(CATONKEYBOARD,message = "bat cat")
pygame.event.post(my_event)
#place a new event on the queue
#把这个我们自己定义的事件丢到事件队列里面
#下面用于长注释的方法
whatisthecode = """

     Python的函数定义中有两种特殊的情况，即出现*，**的形式。
     如：def myfun1(username, *keys)或def myfun2(username, **keys)等。
解释：
   *  用来传递任意个无名字参数，这些参数会一个Tuple的形式访问。
   ** 用来处理传递任意个有名字的参数，这些参数用dict来访问。*
"""
for event in pygame.event.get():
	if event.type == CATONKEYBOARD:
   		print event.message


