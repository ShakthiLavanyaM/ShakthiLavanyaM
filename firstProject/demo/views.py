from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def wish(request):
    now = datetime.datetime.now()
    msg = '<h1> Welcome to the first app developed with Django </h1>'
    return HttpResponse(msg + '\nThe time is: ' + str(now))
