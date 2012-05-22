#!/usr/bin/python2

import pygame

import painter

class Weapon(pygame.sprite.Sprite):
  def __init__(self, cX, cY, (rate, hp, bulletType, image), game):
    """Initializes enemy with its coordinates.
        Args:
        cX: x coordinate.
        cY: y coordinate.
    """
    pygame.sprite.Sprite.__init__(self)
    self.cX = cX
    self.cY = cY
    self.bulletType = bulletType
    self.hp = hp
    self.rate = rate
    self.image = image
    self.game = game
    
    self.rect = image.get_rect()
    self.rect.move_ip((cX, cY))
    self.width = image.get_size()[0]
    
    self.tick = 0
    

  def update(self):
    """creates a new bullet with self.rate frequency
      if self.hp <= 0 object removes itself
    """
    if self.hp <= 0:
      self.game.weapons.remove(self)
    self.tick += 1
    if self.tick % self.rate == 0:
      newBullet = Bullet(self.cX, self.cY, 
                         self.game.bulletType[self.bulletType], self.game)
      self.game.bullets.add(newBullet)
      self.tick = 0
      
  def GetDamage(self, damage):
    self.hp -= damage

class Bullet(pygame.sprite.Sprite):
  def __init__(self, cX, cY, (speed, damage, image), game):
    pygame.sprite.Sprite.__init__(self)
    self.cX = cX
    self.cY = cY
    self.damage = damage
    self.speed = speed
    self.image = image
    self.game = game
    
    self.rect = image.get_rect()
    self.rect.move_ip((cX, cY))
    self.width = image.get_size()[0]
    
  def update(self):
    if self.cX <= 0:
      self.game.bullets.remove(self)
    self.rect = self.rect.move(-self.speed, 0)
    self.cX = self.rect[0]
    
  def Damage(self):
    ret = self.damage
    self.game.bullets.remove(self)
    return ret
