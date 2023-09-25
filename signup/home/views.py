from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# def members(request):
#     return HttpResponse("Hello world!")


def login(request):
    temp = loader.get_template('index.html')
    return HttpResponse(temp.render())
