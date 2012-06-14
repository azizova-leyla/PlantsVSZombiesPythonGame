#!/usr/bin/python2

import os
import sys

import pygame


def LoadImageAndScale(name, (w, h)):
  """ 
    Args:
      string name - name of image to load
      size (w,h) - width and height of resulting image
    Returns 
      image, scaled to size
  """
  fullname = os.path.join('data', name)
  try:
    image = pygame.image.load(fullname)
  except pygame.error, message: 
    print "Cannot load image:", name
    raise SystemExit, message
  image = image.convert()
  image = pygame.transform.scale(image, (int(w), int(h)))
  return image


def DrawBackground():
  screen = pygame.display.get_surface()
  screen_width, screen_height = screen.get_size()
  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill((0, 0, 0)) 
  screen.blit(background, (0, 0)) 

def DrawLine(pos, img):
  screen = pygame.display.get_surface()
  screen.blit(img, pos)
  
  
def DisplayGameOver():
  screen = pygame.display.get_surface()
  screen_width, screen_height = screen.get_size()
  background = pygame.Surface(screen.get_size()) 
  background = background.convert()
  background.fill((255, 255, 255)) 
  screen.blit(background, (0, 0)) 
  back = LoadImageAndScale("gameover.png", (screen_width, screen_height / 3))
  screen.blit(back, (0, screen_height / 3))
  
