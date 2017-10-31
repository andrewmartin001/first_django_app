'''helper functions for app'''

def compass_to_degrees(point):
  '''takes a compass bearing an puts it to the angle convention for the compass visualisation where 90 degrees is West and 0 is north
  input:
    point - string, e.g., 'North'
    output - float, e.g., 0
  '''
  if point.strip() == 'North':
    return 0
  elif point.strip() == 'South':
    return 180
  elif point.strip() == 'East':
    return 270
  elif point.strip() == 'West':
    return 90
  elif point.strip() == 'North-East':
    return 315
  elif point.strip() == 'North-West':
    return 45
  elif point.strip() == 'South-East':
    return 225
  elif point.strip() == 'South-West':
    return 135
  else:
    return None 
    
