from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

import datetime, os


# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def current_time(request):
    cur_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return render(request, 'app/current_time.html', {'cur_time': cur_time})

def workdir(request):
    p = os.path.join(settings.BASE_DIR, 'workdir')
    return render(request, 'app/workdir.html', {'path': p})


