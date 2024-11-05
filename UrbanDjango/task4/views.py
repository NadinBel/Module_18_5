from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    pagename = 'Главная'
    context = {
        'pagename': pagename
    }
    return render(request, 'fourth_task/index.html', context)

def store(request):
    pagename = 'Магазин'
    games = ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]
    context = {
        'pagename': pagename,
        'games': games
    }
    return render(request, 'fourth_task/store.html', context)

def basket(request):
    pagename = 'Корзина'
    context = {
        'pagename': pagename
    }
    return render(request, 'fourth_task/basket.html', context)

