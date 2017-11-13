'''testbench for the local database'''

import unittest
import datetime
from local_db import submit_temperature_data, get_temperatures_between_times

class TestScore(unittest.TestCase):
  def setUp(self):
    self.test_eid = '982 091002051654'

  def test_submission_and_retrieval(self):
    temperature = 12.1
    measurement_time = datetime.datetime(2000, 1, 1, 10, 10, 10)
    time_start = datetime.datetime(measurement_time.year, measurement_time.month, measurement_time.day, 0, 0, 1)
    time_end = datetime.datetime(measurement_time.year, measurement_time.month, measurement_time.day, 23, 59, 59)
    submit_temperature_data(temperature, measurement_time)
    temps = get_temperatures_between_times(time_start, time_end)
    assert(temps[0])


if __name__ == '__main__':
  unittest.main()