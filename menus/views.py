from datetime import datetime

from django.shortcuts import render

# Create your views here.
from menus.models import Menu


def index(request):
    today = datetime.now().date()
    context = {'today': today}
    menus = Menu.objects.all()
    context['menus'] = menus
    return render(request, 'menus/index.html', context)


def detail(request, pk):
    menu = Menu.objects.get(id=pk)
    return render(request, 'menus/detail.html',{'menu': menu})