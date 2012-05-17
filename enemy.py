#!/usr/bin/python2

import pygame
from pygame.locals import *
import painter

class Enemy(pygame.sprite.Sprite):
	def __init__(self, cX, cY):
	 	pygame.sprite.Sprite.__init__(self)
		img = "Zombie.jpg"
		self.image, self.rect = painter.loadImage(img)
		screen = pygame.display.get_surface()
		screenWidth, screenHeight = screen.get_size()
		self.image = pygame.transform.scale(self.image, (int(screenWidth * 0.2), screenHeight / 4))
		self.area = screen.get_rect()
		self.cX = cX
		self.cY = cY
		self.rect.move_ip((cX, cY))
		self.width = self.image.get_size()[0]
		self.speed = 10
		print"Enemy spawned at", cX, " ", cY	
		
	def update(self):
		self.rect = self.rect.move(self.speed, 0)
		self.cX = self.rect[0]
