from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# create the following Python function named index.
def index(request):
    return HttpResponse("Hello, world!")
