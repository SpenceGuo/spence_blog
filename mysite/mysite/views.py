from django.http import HttpResponse
from django.shortcuts import render


def startPage(request):
    return HttpResponse("This is the start page of this project...")


def hello(request):
    return HttpResponse("Hello world ! ")


def index(request):
    context = dict({})
    context['hello'] = "hello world in templates!"
    return render(request, 'index.html', context)

