from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^weather2$', views.liveweather2, name='liveweather2'),
    url(r'^weather$', views.liveweather, name='liveweather'),
    url(r'^$', views.index, name='index'),
]
