'''functions for local db submission and query for weather measurements'''
import sqlite3
import datetime

db_path = 'local_weather.db'

def submit_temperature_data(temperature, measurement_time):
  '''submits temperature and measurement time to local database'''
  try:
    db = sqlite3.connect(db_path)
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS
                        temperature_measurements(temperature real, measurement_time, timestamp)''')
    #cursor.execute('DELETE FROM loss_risk WHERE (method = ? AND animal_id = ? AND start_date = ? AND end_date = ?)', (method, animal_id, start_date, end_date))
    cursor.execute('INSERT INTO  temperature_measurements(temperature, measurement_time) VALUES(?,?)', (temperature, measurement_time))
    db.commit()
  except Exception as e:
    db.rollback()
    print e
    raise e
  finally:
    db.close()

def get_temperatures_between_times(time_start, time_end):
  '''queries local database for temperatures and measurement times from current day'''
  try:
    db = sqlite3.connect(db_path)
    cursor = db.cursor()
    cursor.execute('SELECT temperature, measurement_time FROM temperature_measurements WHERE (measurement_time>? AND measurement_time<=?)', (time_start, time_end))
    results = cursor.fetchall()
  except Exception as e:
    db.rollback()
    print e
    raise e
  finally:
    db.close()
  return results

def get_all_temperatures():
  '''queries local database for temperatures and measurement times'''
  try:
    db = sqlite3.connect(db_path)
    cursor = db.cursor()
    cursor.execute('SELECT temperature, measurement_time FROM temperature_measurements')
    results = cursor.fetchall()
  except Exception as e:
    db.rollback()
    print e
    raise e
  finally:
    db.close()
  return results

if __name__=='__main__':
  print get_all_temperatures()