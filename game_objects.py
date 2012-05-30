#!/usr/bin/python2

import pygame

import painter

class GameObject(pygame.sprite.Sprite):
  def __init__(self, cX, cY, hp, image, game):
    """Initializes enemy with its coordinates.
        Args:
        cX: x coordinate.
        cY: y coordinate.
    """
    pygame.sprite.Sprite.__init__(self)
    self.cX = cX
    self.cY = cY
    self.image = image
    self.hp = hp
    
    self.rect = image.get_rect()
    self.rect.move_ip((cX, cY))
    self.width = image.get_size()[0]
    self.game = game


class Enemy(GameObject):
  def __init__(self, cX, cY, (speed, hp, damage, image), game):
    GameObject.__init__(self, cX, cY, hp, image, game)
    self.speed = speed
    self.damage = damage

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
  


class Weapon(GameObject):
  def __init__(self, cX, cY, (rate, hp, bulletType, image), game):
    """Initializes enemy with its coordinates.
        Args:
        cX: x coordinate.
        cY: y coordinate.
    """
    GameObject.__init__(self, cX, cY, hp, image, game)
    self.bulletType = bulletType
    self.rate = rate    
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


class Bullet(GameObject):
  def __init__(self, cX, cY, (speed, damage, image), game):
    GameObject.__init__(self, cX, cY, hp=0, image=image, game=game)
    self.speed = speed
    self.damage = damage
    
  def update(self):
    if self.cX <= 0:
      self.game.bullets.remove(self)
    self.rect = self.rect.move(-self.speed, 0)
    self.cX = self.rect[0]
    
  def Damage(self):
    ret = self.damage
    self.game.bullets.remove(self)
    return ret
