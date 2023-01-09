from django.urls import path
from app2.views import *
app_name='rani'
urlpatterns=[
    path('kutty/',kutty,name='kutty'),
]