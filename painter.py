#!/usr/bin/python2

import os
import sys

import pygame
import pygame.font

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
  
def DrawScore(value):
  screen = pygame.display.get_surface()
  font = pygame.font.Font(None, 50)
  screen_width, screen_height = screen.get_size()
  pos = (screen_width - 50, 0)
  text = font.render(str(value), 1, (0, 80, 10))
  screen.blit(text, pos)

def DrawWeaponChooser(images, img_size):
  screen = pygame.display.get_surface()
  screen_width, screen_height = screen.get_size()
  images_pos = []
  pos = (0, 0)
  for name in images.keys():
    img = LoadImageAndScale(images[name], img_size)
    screen.blit(img, pos)
    images_pos.append(pos)
    pos = (pos[0] + img_size[0] + 5, pos[1])
    if(pos[0] >= screen_width):
      pos = (0, pos[1] + img_size[1]) 
  return images_pos

def DisplayGameOver():
  screen = pygame.display.get_surface()
  screen_width, screen_height = screen.get_size()
  background = pygame.Surface(screen.get_size()) 
  background = background.convert()
  background.fill((255, 255, 255)) 
  screen.blit(background, (0, 0)) 
  back = LoadImageAndScale("gameover.png", (screen_width, screen_height / 3))
  screen.blit(back, (0, screen_height / 3))
  
