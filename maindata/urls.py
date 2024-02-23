from django.contrib import admin
from django.urls import include, path
app_name='maindata'
from .views import createholidaypdf,home
urlpatterns = [
    path('',home,name='home'),
    path('createholidaypdf/',createholidaypdf,name='createholidaypdf'),
]
