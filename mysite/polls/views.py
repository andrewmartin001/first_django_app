# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from get_current_data import get_current_data

from django.http import HttpResponse

def index(request):
  temperature = get_current_data()[2]
  return HttpResponse("The current temperature is " + temperature + "&deg;C")

