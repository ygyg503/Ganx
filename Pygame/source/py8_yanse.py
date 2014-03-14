#!/usr/bin/python
#-*-coding:utf-8-*-

import pygame
from sys import exit
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640,480),0,32)
#screen 为一个surface对象，就是一个画布
all_colors = pygame.Surface((256,256),depth = 32)
#这一步创建一个大小为4096x4096的画布，
#Surface((width, height), flags=0, depth=0, masks=None) -> Surface
#
for r in xrange(256):
	#用法与range完全相同，所不同的是生成的不是一个数组，而是一个生成器。
	print r+1,"out of 256"
	x = (r&15)*256
	# & 按位与
	y = (r>>4)*256
	#>> 表示向移三位
	for g in xrange(256):
		for b in xrange(256):
			all_colors.set_at((x+g,y+b),(r,g,b))
			#set the color value for a single pixel
			#第一个参数为位置，第二个参数是RGB颜色值
pygame.image.save(all_colors,"all_color.bmp")

