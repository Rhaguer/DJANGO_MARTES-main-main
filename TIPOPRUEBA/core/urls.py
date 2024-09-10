from django.urls import path

from .views import *

urlpatterns = [
    path('', Login, name='Login'),  
    path('index/', index, name='index'),
    path('contacto/', contacto, name='contacto'),
]
