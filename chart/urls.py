from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('examp/', example),
    path('2', post2),
    path('3', post3),
    path('4', post4),
    path('5', post5),
    path('6', post6)
]
