from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def apiconnect(request):
    print("apiconnect")
    return HttpResponse('It works!')
