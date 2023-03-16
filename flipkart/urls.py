from django.urls import path
from flipkart.views import *

app_name='flipkart'

urlpatterns=[
    path('asus/',asus,name='asus'),
]