from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    return render(request, 'third_task/index.html')

def store(request):
    return render(request, 'third_task/store.html')

def basket(request):
    return render(request, 'third_task/basket.html')

