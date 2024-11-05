from django.shortcuts import render
from django.views.generic import TemplateView


def index_main(request):
    return render(request, 'index_main.html')

def index_func(request):
    return render(request, 'index_func.html')

class IndexClass(TemplateView):
    template_name = 'index_class.html'

