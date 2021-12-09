from django.http import HttpResponse
from django.shortcuts import render
import datetime

def index(request):
    return render(request, 'webApp/index.html')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
