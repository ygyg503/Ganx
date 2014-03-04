#!/usr/bin/python
#-*-coding:utf-8-*-

background_image_filename = "/home/yg/Pictures/sushiplate.jpg"
#记录图片路径

import pygame
from pygame.locals import *
from sys import exit

mudi = """本段代码是利用事件学习，用户按下键盘方向键，然后移动屏幕中的图片。"""

pygame.init()
screen = pygame.display.set_mode((800,800),0,32)
background = pygame.image.load(background_image_filename)

x,y = 0,0
#move记录移动值
move_x,move_y = 0,0 
	
while True:
	for event in pygame.event.get():
		print "event = ",event.type
		#print K_RIGHT 这样输出，K_RIGHT代表某一个特定的数字
		#print QUIT
		if event.type == QUIT:
			exit()
		#在pygame.event.get()从时间队列中获取事件出来，然后判断是什么类型事件
		#event.get()函数每次执行后返回eventlist
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				move_x = -1
			elif event.key == K_UP:
				move_y = 1
			elif event.key == K_DOWN:
				move_y = -1
			elif event.key == K_LEFT:
				move_x = 1
		elif event.type == KEYUP:
			move_x = 0
			move_y = 0
	x += move_x
	y += move_y
	
	#fill()是Surface对象的一个方法,他代表了'fill Surface with a solid color‘
	#后面的参数代表RGB颜色值,0，0，0 代表黑色，255.255.255代表
	screen.fill((255,255,255))
	
	#blit()文档上这样说明"Draws a source Surface onto this Surface",
	#blit(source, dest, area=None, special_flags = 0) -> Rect
	#source为要贴的surface对象，
	screen.blit(background,(x,y))
	
	#经过实验加入注释掉这个方法，那么就会一团黑。
	#zhege 
    	
	pygame.display.update()
	
