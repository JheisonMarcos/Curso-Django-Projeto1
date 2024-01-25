# from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.


def home(request): 
    return HttpResponse('HOME 1')


def sobre(request): 
    return HttpResponse('sobre 1')


def contato(request): 
    return HttpResponse('contato 1')
