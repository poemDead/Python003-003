from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello Django!")

def year(request, year):
    return HttpResponse(year)

def name(request, **kwargs):
    return HttpResponse(kwargs['name'])

def myyear(request, year):
    return render(request, 'yearview.html')