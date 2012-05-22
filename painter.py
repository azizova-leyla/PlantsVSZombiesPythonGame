#!/usr/bin/python2

import os
import sys

import pygame


def LoadImageAndScale(name, (w, h)):
  """ string name - name of image to load 
      returns image and it's rectangle
  """
  fullname = os.path.join('data', name)
  try:
    image = pygame.image.load(fullname)
  except pygame.error, message: 
    print "Cannot load image:", name
    raise SystemExit, message
  image = image.convert()
  image = pygame.transform.scale(image, (w, h))
  return image

def DrawBackground():
  screen = pygame.display.get_surface()
  screenWidth, screenHeight = screen.get_size()
  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill((0, 0, 0)) 
  screen.blit(background, (0, 0)) 
  back = LoadImageAndScale("grass.jpg", (screenWidth, screenHeight / 4))
  screen.blit(back, (0, screenHeight / 3)) 
  pygame.display.flip() 
  return back
  
def DisplayGameOver():
  screen = pygame.display.get_surface() 
  screenWidth, screenHeight = screen.get_size()
  background = pygame.Surface(screen.get_size()) 
  background = background.convert()
  background.fill((255, 255, 255)) 
  screen.blit(background, (0, 0)) 
  back = LoadImageAndScale("gameover.png", (screenWidth, screenHeight / 3))
  screen.blit(back, (0, screenHeight / 3)) 
  pygame.display.flip() 
  
