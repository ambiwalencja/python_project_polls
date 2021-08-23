from django.urls import path
from . import views

# this file tells which view corresponds to which url
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
]
