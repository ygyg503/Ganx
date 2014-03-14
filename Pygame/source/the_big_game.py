#!/usr/bin/python
#-*-coding:utf-8-*-

import pygame,sys,random

skier_images = ["./src/skier_down.png","./src/skier_rigth1.png","./src/skier_right2.png","./src/skier_left2.png","./src/skier_left1.png"]
#把图片资源放在list里面

class SkierClass(pygame.sprite.Sprite):
	"""
		SkierClass是pygame.sprite.Sprite的subclass
		“sprite”，中文翻译“精灵”，在游戏动画一般是指一个独立运动的画面元素，在pygame中，就可以是一个带有图像（Surface）和大小位置（Rect）的对象。 精灵特别适合用在OO语言中，比如Python。
		一般需要继承这个class，然后加入自己的代码	


	"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("./src/skier_down.png")
		self.rect = self.image.get_rect()
		self.rect.center = [320,100]
		self.angle = 0
	def turn(self,direction):
		self.angle = self.angle + direction
		if self.angle < -2 : self.angle = -2
		if self.angle >  2 : self.angle =  2
		center = self.rect.center
		self.image = pygame.image.load(skier_image[self.angle])
		self.rect.center = center
		speed = [self.angle,6 - abs(self.angle) * 2]
		return speed

class ObstacleClass(pygame.sprite.Sprite):
		def __init__(self,image_file,location,type):
			pygame.sprite.Sprite.__init__(self)			
			self.image_file = image_file
			self.location = location
			self.rect = self.image.get_rect()
			self.rect.center = location
			self.type = type
			self.passed = False
		def scroll(self,t_ptr):
			self.rect.centery = self.location[1] - t_ptr

def create_map(start,end):
	osbtacles = pygame.sprite.Group()
	gates = pygame.sprite.Group()
	locations = []
	for i in range(10):
		row = random.randint(start,end)
		col = random.randint(0,9)
		location = [col*64 + 20,row*64 + 20]
		if not (location in locations):
			locations.append(location)
			type = random.choice(["tree","flag"])
			if type == "tree": img = "./src/skier_tree.png"
			elif type == "flag": img = "./src/skier_flag.png"
			obstacle = ObstacleClass(img,location,type)
			obstacle.add(obstacle)
	return obstacles

def animate():
	screen.fill([255,255,255])
	pygame.display.update(obstacles.draw(screen))
	screen.blit(skier.image,skier.rect)
	screen.blit(score_text,[10,10])
	pygame.display.flip()

def updateObstacleGroup(map0,map1):
	obstacles = pygame.sprite.Group()
	for ob in map0:	obstacles.add(ob)
	for ob in map1: obstacles.add(ob)
	return obstacles

pygame.init()
screen = pygame.display.set_mode([640,640])
clock = pygame.time.Clock()
#创建一个Clock对象，对象有5个方法，获取从pygame.init()开始的时间，或者让process wait一会
skier = SkierClass()
#创建一个skierCla
speed = [0,6]
map_position = 0
points = 0
map0 = create_map(20,29)
map1 = create_map(10,19)
activeMap = 0
obstacles = updateObastacleGroup(map0,map1)
font = pygaem.font.Font(None,50)

while True:
	clock.tick(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				speed = skier.turn(-1)
			elif event.key == pygame.K_RIGHT:
				speed = skier.turn(1)
	skier.move(speed)
	map_position += speed[1]
	
	if map_positon >= 640 and activeMap == 0:
		activeMap = 1
		map0 = create_map(20,29)
		obstacles = updateObastacleGroup(map0,map1)
	if map_position >= 1280 and activeMap == 1:
		activeMap = 0
		for ob in map0:
			ob.location[1] = ob.location[1] -1280
		map_position = map_position -1280
		map1 = create_map(10,19)
		obstacles = updateObastacleGroup(map0,map1)
	
	for obstacle in obstacles:
		obstacle.scroll(map_position)
	hit = pygame.sprite.spritecollide(sker,obstacles,False)
	if hit:
		if hit[0].type == "tree" and not hit[0].passed:
			points = points - 100
			skier.image = pygame.image.load("skier_crash.png")
			animate()
			pygame.time.delay(1000)
			skier.image = pygame.image.load("skier_down.png")
			skier.angle = 0
			speed = [0,6]
		elif hit[0].type == "flag" and not hit[0].passed:
			points += 10
			obstacles.remove(hit[0])
	score_text = font.render("Score :"+str(points),1,(0,0,0))
	animate()
