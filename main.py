#!/usr/bin/python2

import sys
import pygame
from pygame.locals import *
import painter
import enemy

def init_window():
	pygame.init()
	window = pygame.display.set_mode((1000, 550))
	pygame.display.set_caption('The Game')
 
def input(events):
	for event in events:
		if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
			sys.exit(0)
		else:
			pass
def check(creatures, endLocation):
	for creature in creatures:
		if creature.cX + creature.width >= endLocation:
			return 1
	return 0
 
def action(speed, endLocation):
	creatures_list = []
	screen = pygame.display.get_surface()
	screenWidth, screenHeight = screen.get_size()
	zombie = enemy.Enemy(0, screenHeight / 3) 
	creatures_list.append(zombie)
	creatures = pygame.sprite.RenderPlain(creatures_list)
	clock = pygame.time.Clock()
	while 1:
		clock.tick(float(speed))
		input(pygame.event.get())
		if check(creatures_list, endLocation) == 1:
			painter.displayGameOver()
		else:
			creatures.update() 
			painter.drawBackground()
			creatures.draw(screen)		
			pygame.display.flip()
		

 
def main():
	init_window()
	speed = 4
	endLocation = pygame.display.get_surface().get_size()[0]
	if len(sys.argv) > 1:
		speed = sys.argv[1]
	action(speed, endLocation)
 
if __name__ == '__main__': main()
