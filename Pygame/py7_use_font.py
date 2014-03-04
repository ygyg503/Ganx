#!/usr/bin/python
#-*-coding:utf-8-*-
import pygame
from sys import exit
from pygame.locals import *

#这段代码目的是把一段文字变为图片
#基本过程为:Font->Surface->图片

pygame.init()

#print system can use all font
#因为get_fonts()返回list,将其转化为string,string.join()方法先将list所有字符串连接，并且按照前面的规则分割.
all_fonts = '<-->'.join(pygame.font.get_fonts())

#use system font,pasans是系统自带的一种字体,转换后system_font是Font对象
system_font = pygame.font.SysFont("ptsans",25)

#uer my font
FONT_PATH = "/home/yg/Pygame/youyuan.ttf"
FONT_SIZE = 25
my_font = pygame.font.Font(FONT_PATH,FONT_SIZE)

#change to Surface
text_surface = system_font.render(all_fonts[1:50],True,(255,255,255))
#上一行代码作用把Font对象转化成为surface对象
pygame.image.save(text_surface,"test_surface.jpg")
#image.save()方法是传一个serface对象和其他参数过去，然后它保存成图片文件到文件系统中
#image.load()则是把文件系统中的图片载入，然后返回surface对象

my_font_surface = my_font.render("Python is Cool",True,(255,255,255))
pygame.image.save(my_font_surface,"test_2.jpg")

 
