from django.urls import path
from app1.views import *
app_name='raja'
urlpatterns=[
    path('chinnu/',chinnu,name='chinnu'),
]