#!/usr/bin/python2.7

import collections
import unittest

import game_objects
import util


class TestGameLogic(unittest.TestCase):
  def setUp(self):
    self.callback_called = False

  def test_weapon_creates_bullet(self):    
    image = None
    rate = 3
    weapon_hp = 10

    x, y = 10, 20
    def BulletCallback(cX, cY):
      self.callback_called = True
      self.assertEqual(cX, x)
      self.assertEqual(cY, y)

    weapon = game_objects.Weapon(x, y, rate, weapon_hp, image,
                                 BulletCallback)
    # As far as the rate equals 3,
    # the callback is expected to be called on 3rd step
    weapon.update()
    self.assertFalse(self.callback_called)

    weapon.update()
    self.assertFalse(self.callback_called)

    weapon.update()
    self.assertTrue(self.callback_called)

  def test_enemy_meets_bullet(self):
    enemy_speed = 0
    enemy_hp = 100
    enemy_damage = 0

    enemy = game_objects.Enemy(0, 0,
                               enemy_speed, enemy_hp, enemy_damage, None)
    bullet_speed = 5
    bullet_damage = 50
    bullet = game_objects.Bullet(10, 0, bullet_speed, bullet_damage, None)

    enemy.update()
    bullet.update()
    util.ProcessDamage([bullet], [enemy])
    self.assertEqual(enemy.hp, enemy_hp)
    self.assertEqual(bullet.hp, bullet_damage)

    enemy.update()
    bullet.update()
    util.ProcessDamage([bullet], [enemy])

    self.assertEqual(enemy.hp, enemy_hp - bullet_damage)
    self.assertEqual(bullet.hp, 0)

  def test_intersect(self):
    MyObject = collections.namedtuple('MyObject', ['cX', 'width'])
    self.assertTrue(util.Intersect(MyObject(0, 0), MyObject(0, 0)))
    
  def test_inside(self):
    point = (1, 1)
    polygon_left_down_corner = (-1, -1)
    polygon_size = (2, 2)
    self.assertTrue(util.Inside(point, polygon_left_down_corner, polygon_size))
  
  def test_not_inside(self):
    point = (-10, 10)
    polygon_left_down_corner = (-1, -1)
    polygon_size = (2, 2)
    self.assertFalse(util.Inside(point, polygon_left_down_corner, polygon_size))


if __name__ == '__main__':
  unittest.main()
