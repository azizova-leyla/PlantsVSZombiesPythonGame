#!/usr/bin/python2.7

def Intersect(x, y):
  """Checks if segments intersect in 1D-space."""
  return min(x.cX + x.width, y.cX + y.width) >= max(x.cX, y.cX)


def ProcessDamage(damage_dealer, damage_taker):
  """Process damage from damage_dealer to damage_taker if they intersects."""
  for x in damage_dealer:
    for y in damage_taker:
      if Intersect(x, y):
        y.GetDamage(x.Damage())
