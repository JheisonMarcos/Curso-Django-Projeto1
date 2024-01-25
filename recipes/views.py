from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'recipes/home.html', contex={
        'name': 'Jheison Francelino',
    })


def sobre(request):
    return HttpResponse('sobre 1')


def contato(request):
    return render(request, 'temp.html')
