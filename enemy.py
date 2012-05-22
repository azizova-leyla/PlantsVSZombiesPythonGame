#!/usr/bin/python2

import pygame

import painter

class Enemy(pygame.sprite.Sprite):
  def __init__(self, cX, cY, (speed, image)):
    """Initializes enemy with its coordinates.
        Args:
        cX: x coordinate.
        cY: y coordinate.
    """
    pygame.sprite.Sprite.__init__(self)
    self.cX = cX
    self.cY = cY
    self.rect = image.get_rect()
    self.rect.move_ip((cX, cY))
    self.width = image.get_size()[0]
    self.speed = 10
    self.image = image
    print "Time is ", pygame.time.get_ticks()," Enemy spawned at", cX, " ", cY

  def update(self):
    """move object to the right to self.speed pixels
    """
    self.rect = self.rect.move(self.speed, 0)
    self.cX = self.rect[0]
