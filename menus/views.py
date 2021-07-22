from datetime import datetime

from django.shortcuts import render

# Create your views here.

def index(request):
    today = datetime.now().date()
    context = {'today': today}
    return render(request, 'menus/index.html', context)


def detail(request, menu):
    return render(request, 'menus/detail.html')