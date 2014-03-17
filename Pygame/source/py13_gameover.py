#-*-coding:utf-8-*-
import pygame,pygame.locals
from sys import exit

#resource in here
background_image = "/home/yg/Pictures/xxx.jpg"
#init the pygame
pygame.init()

#make a Surface object
screen = pygame.display.set_mode((800,480),0,32)
pygame.display.set_caption("The Part of Game.")

#make a Font object
game_font = pygame.font.SysFont("",46)

#the say goodbye str

#turn the font to Surface Object
font_surface = game_font.render("Game Over!",True,(0,0,0))

#postion font
font_y = (480 - font_surface.get_height()) / 2
font_x = (800 - font_surface.get_width()) / 2
print "480 - "+str(font_surface.get_height())
print "800 - "+str(font_surface.get_width())
print font_x,font_y
#loca the pictures
background = pygame.image.load(background_image) 

#while-loop 
while True:
	for user_event in pygame.event.get():
		if user_event.type == pygame.locals.QUIT:
			exit()
	#pictures to the surface object
	screen.blit(background,(0,0))
	
	font_y -= 0.3
	print "font_y = ",font_y

	if font_y < 0:
		font_y = 480 + font_y
	print font_y

	#font to screen
	screen.blit(font_surface,(font_x,font_y))
	
	#update surface
	pygame.display.update()



