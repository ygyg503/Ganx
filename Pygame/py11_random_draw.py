#!/usr/bin/pytho
#-*-coding:utf-8-*-
#代码目的: 利用randint()函数产生随机数，然后即可作为随机坐标，然后在画布上随机任意位置花任意大小的圆形
import pygame
from random import * # 这个主要为了生产出随机数
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,480),0,32)
pygame.display.set_caption("Testing random and draw ")

#
for i in range(0,100):
	#利用randint()函数随机产生区间大小的数字，座标随机，半径随机，颜色随机
	circle_postion = (randint(0,800),randint(0,480)) 
	radius = randint(0,160)
	circle_color = (randint(0,255),randint(0,255),randint(0,255))
	pygame.draw.circle(screen,circle_color,circle_postion,radius)
	#pygame.draw.circle()为了在画布(surface对象上画圆形
	#circle(Surface, color, pos, radius, width=0) -> Rect
	pygame.display.update()

while True:
	for event in pygame.event.get():
	#事件测试，获取事件队列里面的事件
		if event.type == QUIT:
		#当事件类型为退出时候，一般是按下X图标时候
			over_font = pygame.font.SysFont("",32)
			#产生字体Font对象
			font_surface = over_font.render("Game Over!",True,(255,255,255))
			#由字体产生surface对象			
			screen.blit(font_surface,(380,220))
			#把字体对象贴到画布上，就是在屏幕上现实Game Over
			pygame.display.update()
			#当然，需要更新画布才看得见
		else:
			pass
			

