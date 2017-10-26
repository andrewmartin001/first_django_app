import urllib2

path = "http://www.physics.otago.ac.nz/eman/weather_station/weather_data/WX_CURRENT.DAT"

def get_current_data():
  '''gets the current weather data from the otago weather station'''
  web = urllib2.urlopen(path)
  content = web.read().split('\r\n')
  web.close()
  return content

if __name__ == '__main__':
  data = get_current_data()
  print 't=', data[2]