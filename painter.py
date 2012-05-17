#!/usr/bin/python2

import sys
import pygame
import os
import Image
from pygame.locals import *

def loadImage(name):
	fullname = os.path.join('data', name)
	try:
		  image = pygame.image.load(fullname)
	except pygame.error, message: 
		  print "Cannot load image:", name
		  raise SystemExit, message
	image = image.convert() 
	return image, image.get_rect()

def drawBackground():
	screen = pygame.display.get_surface() 
	screenWidth, screenHeight = screen.get_size()
	background = pygame.Surface(screen.get_size()) 
	background = background.convert()
	background.fill((0, 0, 0)) 
	screen.blit(background, (0, 0)) 
	back, back_rect = loadImage("grass.jpg") 
	back = pygame.transform.scale(back, (int(screenWidth * 0.8), screenHeight / 4))
	screen.blit(back, (int(screenWidth * 0.2), screenHeight / 3)) 
	pygame.display.flip() 
	return back
  
def displayGameOver():
	screen = pygame.display.get_surface() 
	screenWidth, screenHeight = screen.get_size()
	background = pygame.Surface(screen.get_size()) 
	background = background.convert()
	background.fill((255, 255, 255)) 
	screen.blit(background, (0, 0)) 
	back, back_rect = loadImage("gameover.png") 
	back = pygame.transform.scale(back, (screenWidth, screenHeight / 3))
	screen.blit(back, (0, screenHeight / 3)) 
	pygame.display.flip() 
