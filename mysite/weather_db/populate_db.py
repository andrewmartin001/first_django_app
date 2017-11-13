'''functions that put weather data in the local database and plot days data. Also plot weather data'''

from local_db import submit_temperature_data, get_temperatures_between_times
from get_current_data import get_current_data
import datetime
import plotly.plotly as py
import plotly.graph_objs as go

def populate_database():
  '''populates local database with latest measurements from physics department'''
  data = get_current_data()
  temperature = data[2]
  date = data[0]
  time = data[1]
  #print date+'/'+time
  datetime_object = datetime.datetime.strptime(date + '/' + time, '%d/%m/%Y/%H:%M')
  #print datetime_object
  submit_temperature_data(temperature, datetime_object)

def plot_slider(x_data, y_data, x_title, y_title, filename):
    '''plots a scatter plot'''
    trace = go.Scatter(x=x_data,
                       y=y_data)

    data = [trace]
    layout = dict(
        xaxis=dict(
            title=x_title,
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label='1m',
                         step='month',
                         stepmode='backward'),
                    dict(count=6,
                         label='6m',
                         step='month',
                         stepmode='backward'),
                    dict(count=1,
                        label='YTD',
                        step='year',
                        stepmode='todate'),
                    dict(count=1,
                        label='1y',
                        step='year',
                        stepmode='backward'),
                    dict(step='all')
                ])
            ),
            rangeslider=dict(),
            type='date'
        ),
        yaxis=dict(
            title=y_title
        )
    )
    fig = dict(data=data, layout=layout)
    py.plot(fig, filename = filename, auto_open=False)

def plot_temperature_data():
  '''gets temperature data for current day and plots using plotly'''
  data_now = get_current_data()
  date = data_now[0]
  time = data_now[1]
  measurement_time = datetime.datetime.strptime(date + '/' + time, '%d/%m/%Y/%H:%M')
  #the start and end of the current day
  time_start = datetime.datetime(measurement_time.year, measurement_time.month, measurement_time.day, 0, 0, 1)
  time_end = datetime.datetime(measurement_time.year, measurement_time.month, measurement_time.day, 23, 59, 59)
  data = get_temperatures_between_times(time_start, time_end)
  print data
  filename = 'days_temps'
  temps = [element[0] for element in data]
  dates = [element[1] for element in data]
  plot_slider(dates, temps, 'time', 'temperature (C)', filename)



if __name__=='__main__':
  populate_database()
  plot_temperature_data()