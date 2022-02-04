
from django.urls import path,include
from .views import calendar

urlpatterns = [
    path('', calendar,name='calendar')
]
