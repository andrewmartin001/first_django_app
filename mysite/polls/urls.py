from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^weather2$', views.liveweather2, name='liveweather2'),
    url(r'^weather$', views.weather, name='weather'),
    url(r'^sensors$', views.sensors, name='sensors'),
    url(r'^research$', views.research, name='research'),
    url(r'^$', views.index, name='index'),
]
