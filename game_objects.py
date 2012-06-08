#!/usr/bin/python2

import pygame

import painter

class GameObject(pygame.sprite.Sprite):
  def __init__(self, cX, cY, hp, image):
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
    
    if image:
      self.rect = image.get_rect()
      self.width = image.get_size()[0]
    else:
      self.rect = pygame.Rect(0, 0, 0, 0)
      self.width = 0
    self.rect.move_ip((cX, cY))
  
  def IsAlive(self):
    return self.hp > 0


class Enemy(GameObject):
  def __init__(self, cX, cY, (speed, hp, damage, image)):
    GameObject.__init__(self, cX, cY, hp, image)
    self.speed = speed
    self.damage = damage

  def update(self):
    """move object to the right to self.speed pixels
    """
    self.rect = self.rect.move(self.speed, 0)
    self.cX = self.rect[0]
    
  def GetDamage(self, damage):
    self.hp -= damage
    
  def Damage(self):
    return self.damage


class Weapon(GameObject):
  def __init__(self, cX, cY, (rate, hp, image), bullet_callback):
    """Initializes enemy with its coordinates.
        Args:
        cX: x coordinate.
        cY: y coordinate.
    """
    GameObject.__init__(self, cX, cY, hp, image)
    self.rate = rate
    self.tick = 0
    self.bullet_callback = bullet_callback

  def update(self):
    """creates a new bullet with self.rate frequency
      if self.hp <= 0 object removes itself
    """
    self.tick += 1
    if self.tick % self.rate == 0:
      self.bullet_callback(self.cX, self.cY)
      self.tick = 0
      
  def GetDamage(self, damage):
    self.hp -= damage


class Bullet(GameObject):
  def __init__(self, cX, cY, (speed, damage, image)):
    GameObject.__init__(self, cX, cY, hp=damage, image=image)
    self.speed = speed
    
  def IsAlive(self):
    return GameObject.IsAlive(self) and self.cX > 0
    
  def update(self):
    self.rect = self.rect.move(-self.speed, 0)
    self.cX = self.rect[0]
    
  def Damage(self):
    ret = self.hp
    self.hp = 0
    # self.game.bullets.remove(self)
    return ret
