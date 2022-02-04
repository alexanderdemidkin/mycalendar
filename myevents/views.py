from django.shortcuts import render
from .models import My_event
from .utils import ModelCalendar
import datetime


def calendar(request):
    context = {}
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month

    calendar = ModelCalendar(year=year, month=month).formatyear(year,My_event)
    context['calendar']=calendar
    url = 'index.html'
    return render(request, url, context)