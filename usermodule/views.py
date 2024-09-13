from django.shortcuts import render

# Create your views here.
def index3(request):
    return render(request, 'index3.html',{'name' : 'Majed'})