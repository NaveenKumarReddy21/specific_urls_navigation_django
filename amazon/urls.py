from django.urls import path
from amazon.views import *
app_name='amazon'

urlpatterns=[
    path('asus/',asus,name='asus'),
]