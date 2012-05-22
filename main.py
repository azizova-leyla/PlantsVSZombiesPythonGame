#!/usr/bin/python2

import sys

import pygame
from pygame import locals

import painter
import enemy

DEFAULT_GAME_SPEED = 4 #ticks per second
HTAB_SIZE = 0.2 #in percents
VTAB_SIZE = 0.25 #in percents
ENEMY_SPAWN_FREQUENCY = 20 #in ticks
ENEMY_TYPES = 1

class Game():
  def __init__(self, speed):
    pygame.init()
    window = pygame.display.set_mode((1000, 550))
    pygame.display.set_caption('The Game')
    
    self.enemies = AllEnemies()
    self.weapons = AllWeapons()
    self.bullets = AllBullets()
    
    self.speed = float(speed)
    
    self.width, self.height = pygame.display.get_surface().get_size()
    self.endLocation = self.width
    self.clock = pygame.time.Clock()
    self.fieldTop = self.height / 3
    
    #Enemies types properties
    self.enemyType = []
    self.enemyType.append((10, painter.LoadImageAndScale("Zombie.jpg",
                                 (int(self.width * HTAB_SIZE),
                                 int(self.height * VTAB_SIZE)))))

  def KeyboardInput(self, events):
    for event in events:
      if ((event.type == locals.QUIT) or 
      (event.type == locals.KEYDOWN and event.key == locals.K_ESCAPE)):
        return False
    return True

  def IsGameOver(self):
    """checks if at least one of the enemies touches endLocation 
      Args:
        list creatures - list of game objects
        int endLocation - x coordinate of position where game overs 
      Returns:
        True if the game is over
    """
    return any(c.cX + c.width >= self.endLocation for c in self.enemies)

  def TrySpawnEnemy(self):
    """creates new Enemy, according to time plan
      Returns:
        True if Enemy was spawned
        False if it's not time for the new Enemy
    """
    if((pygame.time.get_ticks() / self.clock.get_time()) % ENEMY_SPAWN_FREQUENCY == 0):
      lineNumber = 0 #here may be some random if there is more than one line
      type = 0 #here may be random also
      newEnemy = enemy.Enemy(0, self.fieldTop + lineNumber * VTAB_SIZE, 
                       self.enemyType[type])
      self.enemies.add(newEnemy)
      return True
    return False
  
  def UpdateAll(self):
    self.TrySpawnEnemy()
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
    """The main loop of the game
        Args:
          float speed - amount of ticks in one second 
          int endLocation - x coordinate of position where game overs 
    """

    while 1:
      self.clock.tick(self.speed)
      
      if(self.KeyboardInput(pygame.event.get()) == False):
        return
        
      if self.IsGameOver() == True:
        painter.DisplayGameOver()
      else:
        self.UpdateAll()
        self.DrawAll()


class AllEnemies(pygame.sprite.RenderUpdates):
  def __init__(self):
    pygame.sprite.RenderUpdates.__init__(self)


class AllWeapons(pygame.sprite.RenderUpdates):
  def __init__(self):
    pygame.sprite.RenderUpdates.__init__(self)

class AllBullets(pygame.sprite.RenderUpdates):
  def __init__(self):
    pygame.sprite.RenderUpdates.__init__(self)

def main():
  speed = DEFAULT_GAME_SPEED
  if len(sys.argv) > 1:
    speed = sys.argv[1]
  game = Game(speed)
  game.ProcessGame()

if __name__ == '__main__': main()
