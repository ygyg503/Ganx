#!/usr/bin/python
#-*-coding:utf-8-*-

#这段代码目的是创建一个可以改变大小的图形窗口

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#定义素材的位置
background_image_filename = "/home/yg/Pictures/1.jpg"
background = pygame.image.load(background_image_filename).convert() 

#定义窗口的大小
windows_size = background.get_size()

screen = pygame.display.set_mode(windows_size,RESIZABLE,32)
#RESIEABLE代表窗口大小可以调节


while True:
	#收集事件
	event = pygame.event.wait()
	if event.type == QUIT:
		exit()
	if event.type == VIDEORESIZE:
		vindows_size = event.size
		screen=pygame.display.set_mode(windows_size,RESIZABLE,32)
		pygame.display.set_caption("Window resize to " + str(event.size))
		
	screen_width,screen_height = windows_size
		
	for y in range(0,screen_height,background.get_height()):
		for x in range(0,screen_width,background.get_width()):
			screen.blit(background,(x,y))
	pygame.display.update()
