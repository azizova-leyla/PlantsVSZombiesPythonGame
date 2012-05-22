#!/usr/bin/python2

import pygame

import main
import painter

class Enemy(pygame.sprite.Sprite):
  def __init__(self, cX, cY, (speed, hp, damage, image), game):
    """Initializes enemy with its coordinates.
        Args:
        cX: x coordinate.
        cY: y coordinate.
    """
    pygame.sprite.Sprite.__init__(self)
    self.cX = cX
    self.cY = cY
    self.speed = speed
    self.image = image
    self.hp = hp
    self.damage = damage
    
    self.rect = image.get_rect()
    self.rect.move_ip((cX, cY))
    self.width = image.get_size()[0]
    self.game = game

  def update(self):
    """move object to the right to self.speed pixels
    """
    if self.hp <= 0:
      self.game.enemies.remove(self)
      
    self.rect = self.rect.move(self.speed, 0)
    self.cX = self.rect[0]
    
  def GetDamage(self, damage):
    self.hp -= damage
    
  def Damage(self):
    return self.damage
  
