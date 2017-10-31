# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from get_current_data import get_current_data

from django.http import HttpResponse
from polls.utils import compass_to_degrees

def index(request):
  temperature = get_current_data()[2]
  return HttpResponse("The current temperature is " + temperature + "&deg;C")

def liveweather(request):
  temperature = get_current_data()[2]
  return render(request, 'polls/liveweather.html', {'temperature': temperature})

def liveweather2(request):
  temperature = get_current_data()[2]
  wind_speed = get_current_data()[9]
  wind_direction = get_current_data()[10]
  wind_direction = compass_to_degrees(wind_direction)
  return render(request, 'polls/liveweather2.html', {'temperature': temperature, 'wind_speed': wind_speed, 'wind_direction': wind_direction})

def detail(request, question_id):
  return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)
