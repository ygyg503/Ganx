#!/usr/bin/python
#-*-coding:utf-8-*-
import pygame
from sys import exit
from pygame.locals import *

pygame.init()
Pic = (449,300)
#记录图片分辨率，为了填充好窗口
screen = pygame.display.set_mode(Pic,0,32)
pygame.display.set_caption("Fullscreen Testing")
#设置窗口的标题
background_image_filename = "/home/yg/Pictures/1.jpg"
background = pygame.image.load(background_image_filename).convert()
Fullscreen =  False

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type == KEYDOWN:
			#当事件类型为键盘按下时候，event会有三个属性，unicode,key,mod，unicode会记录按了哪个键，
			#可以用print str(event)打印出来看上面的几个属性信息，
			print str(event)
			if event.unicode == u'f':
			#判断是否按了这个键，按了的话符合条件然后就设置全屏幕
				Fullscreen = not Fullscreen 
				#Fullscreen用的太机智了，下一次按就会符合另外一个条件，达到按F可以交替全/非全屏幕
				if Fullscreen:					
					screen = pygame.display.set_mode(Pic,FULLSCREEN,32)
				else:
					screen = pygame.display.set_mode(Pic,0,32)
	screen.blit(background,(0,0)) 
	#把背景图片花到surface对象(屏幕那个框框)上。
	pygame.display.update()
	#每次循环都更新一下

