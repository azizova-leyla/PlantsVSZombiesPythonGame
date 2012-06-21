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

        
def Inside(point, polygon_left_down_corner, polygons_size):
  polygon_up_right_corner = (polygon_left_down_corner[0] + polygons_size[0],
                             polygon_left_down_corner[1] + polygons_size[1])
  return (point[0] >= polygon_left_down_corner[0] and
          point[1] >= polygon_left_down_corner[1] and
          point[0] <= polygon_up_right_corner[0] and
          point[1] <= polygon_up_right_corner[1])


def InWhatPolygonIsPoint(point, polygons_corner, polygons_size):
  i = 0
  for polygon_left_down_corner in polygons_corner:
    if Inside(point, polygon_left_down_corner, polygons_size):
      return i
    i = i + 1
  return -1
