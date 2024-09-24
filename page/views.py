from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello, World!??')
def index4(request):
    return render(request, 'pagees/index4.html')