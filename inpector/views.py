from django.shortcuts import render

from django.http import HttpResponse
#import method for returning json response
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest

def index(request):
    print(request.headers)
    print(request.body)
    return HttpResponse("Hello, world. You're at the polls index.")