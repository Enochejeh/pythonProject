from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("hello world")

def about(request):
    return HttpResponse("you have hit about us")

def contact(request):
    return HttpResponse("contact us")

