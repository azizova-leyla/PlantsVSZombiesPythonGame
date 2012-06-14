#!/usr/bin/python2.7

import sys

import pygame
from pygame import locals

import game_objects
import painter
import util

DEFAULT_GAME_SPEED = 4 #ticks per second
HTAB_SIZE = 0.2 #in percents
VTAB_SIZE = 0.25 #in percents
ENEMY_SPAWN_FREQUENCY = 20 #in ticks
BULLET_SIZE = 20


class Game():
  def __init__(self, speed):
    pygame.init()
    window = pygame.display.set_mode((1000, 550))
    pygame.display.set_caption('The Game')
    
    self.enemies = pygame.sprite.RenderUpdates()
    self.weapons = pygame.sprite.RenderUpdates()
    self.bullets = pygame.sprite.RenderUpdates()

    self.speed = speed

    self.width, self.height = pygame.display.get_surface().get_size()
    self.endLocation = self.width
    self.clock = pygame.time.Clock()
    self.fieldTop = self.height / 3

  def MakeZombie(self, cX, cY):
    return game_objects.Enemy(
        cX, cY, speed=10, hp=10, damage=10,
        image=painter.LoadImageAndScale("Zombie.jpg",
                                        (self.width * HTAB_SIZE,
                                         self.height * VTAB_SIZE)))

  def MakeSunFlowerWeapon(self, cX, cY):
    def AddBullet(cX, cY):
      new_bullet = game_objects.Bullet(
          cX, cY, speed=20, damage=5,
          image=painter.LoadImageAndScale("B1.jpg", (BULLET_SIZE,
                                                     BULLET_SIZE)))
      self.bullets.add(new_bullet)

    new_weapon = game_objects.Weapon(
        cX, cY,
        rate=10, hp=10,
        image=painter.LoadImageAndScale("W1.jpg",
                                        (self.width * HTAB_SIZE,
                                         self.height * VTAB_SIZE)),
        bullet_callback=AddBullet)
    return new_weapon

  def KeyboardInput(self, events):
    for event in events:
      if ((event.type == locals.QUIT) or 
          (event.type == locals.KEYDOWN and event.key == locals.K_ESCAPE)):
        return False
    return True

  def IsGameOver(self):
    """Checks if at least one of the enemies touches endLocation.

      Returns:
        True if the game is over
    """
    return any(c.cX + c.width >= self.endLocation for c in self.enemies)

  def TrySpawnEnemy(self):
    """Creates new Enemy, according to time plan.

      Returns:
        Boolean indicating whether an enemy was spawn.
    """
    if ((pygame.time.get_ticks() / self.clock.get_time()) % 
         ENEMY_SPAWN_FREQUENCY == 0):
      lineNumber = 0 #here may be some random if there is more than one line
      type = 0 #here may be random also
      newEnemy = self.MakeZombie(0, self.fieldTop + 
                                 lineNumber * VTAB_SIZE * self.height)
      self.enemies.add(newEnemy)
      return True
    return False
    
  def CreateWeapon(self, line_number, weapon_type):
    cX = int(self.width * (1 - HTAB_SIZE))
    cY = self.fieldTop + line_number * VTAB_SIZE * self.height

    weapon = weapon_type(cX, cY)
    self.weapons.add(weapon)
  
  def UpdateAll(self):
    self.TrySpawnEnemy()
    util.ProcessDamage(self.bullets, self.enemies)
    util.ProcessDamage(self.enemies, self.weapons)
    
    for group in [self.enemies, self.weapons, self.bullets]:
      for element in group:
        if not element.IsAlive():
          group.remove(element)
    
    self.enemies.update()
    self.weapons.update()
    self.bullets.update()
    
  def DrawAll(self):
    painter.DrawBackground()
    self.enemies.draw(pygame.display.get_surface())
    self.weapons.draw(pygame.display.get_surface())
    self.bullets.draw(pygame.display.get_surface())
    pygame.display.flip()

  def ProcessGame(self):
    """The main loop of the game."""

    self.CreateWeapon(line_number=0, weapon_type=self.MakeSunFlowerWeapon)
    while self.KeyboardInput(pygame.event.get()):
      self.clock.tick(self.speed)
      
      if self.IsGameOver():
        painter.DisplayGameOver()
      else:
        self.UpdateAll()
        self.DrawAll()


def main():
  speed = DEFAULT_GAME_SPEED
  if len(sys.argv) > 1:
    speed = sys.argv[1]
  game = Game(speed)
  game.ProcessGame()


if __name__ == '__main__':
  main()
