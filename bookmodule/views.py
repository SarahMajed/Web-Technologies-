from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index1(request):
    return render(request, 'index1.html',{'name' : 'Sarah'})


def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "index1.html", {"name": name})  

    return HttpResponse("Hello, " + name)
 
def index2(request, val1 = 0):   #add the view function (index2)
    return HttpResponse("value1 = "+str(val1))
    
def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'show.html', context)

def index5(request):
 return render(request, 'index5.html')

def list_books(request):
 return render(request, 'list_books.html')

def viewbook(request, bookId):
 return render(request, 'one_book.html')

def aboutus(request):
 return render(request, 'aboutus.html')

def one_book(request):
 return render(request, 'one_book.html')