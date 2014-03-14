#-*-coding:utf-8-*-
import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
#初始化，整出一个大电子画板
font = pygame.font.SysFont(None,64)
#分配一个字体管理员，负责字体工作
text_surface = font.render("Game Over.",True,(244,244,244))
#让字体管理员帮你打印GCD wansui，并且字体滑一点，颜色为xx
#然后字体管理员还给你了一张有字的电子画板
x = (640 - text_surface.get_width()) / 2
y = (480 - text_surface.get_height()) / 2
#这个是为了等下告诉大号电子画板，你把小画板贴到你的哪个位置？

background = pygame.image.load("/home/yg/Pictures/xxx.jpg").convert()
#大号画板需要背景壁纸嘛，那就把图片文件转换成图片电子画板咯

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
	#event是个哨兵，能知道用户你丫的情报，按下键盘，点击鼠标..你被侦察了
	#event.type = exit 表示用户你丫点x 图标，当然关闭退出咯
	screen.blit(background,(0,0))
	#丫的把背景壁纸给我放到大电子画板上
	
	#x -= 0.1
	#循环因此位置-2，明显为了如电影结束的字幕一样滚动,

	#if x < -text_surface.get_width():
	#	x = 640 - text_surface.get_width()

	y -= 0.05
	if y < -text_surface.get_height():
		y = 480 - text_surface.get_height()
	
	screen.blit(text_surface,(x,y))
	#丫的把带字的画板也放上去
	pygame.display.update()
 
