from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from .models import Student,Address, ImageModel
from django.shortcuts import redirect
from .forms import AddressForm , StudentForm , ImageForm


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

def html5_links(request):
  return render(request, 'links.html')

def format(request):
  return render(request, 'format.html')

def list(request):
  return render(request, 'list.html')

def table(request):
  return render(request, 'table.html')

def search(request):
  
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        
        # Fetch books and filter based on input
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            
            if contained:
                newBooks.append(item)
        return render(request, 'bookList.html', {'books': newBooks})
    
    return render(request, 'search.html')


def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

#def __str__(self):
  # return self.name

def query(request):
    mybooks=Book.objects.filter(title__icontains='d') # <- multiple objects
    return render(request, 'query.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='a').filter(edition__gte = 2).exclude(price__lte = 50)[:10]
    if len(mybooks)>=1:
        return render(request, 'query.html', {'books':mybooks})
    else:
        book1= Book.objects.all()
        return render(request, 'filter.html')

def task1_view(request):
    books = Book.objects.filter(Q(price__lte=50))
    return render(request, 'task1.html', {'books': books})

def task2_view(request):
    books = Book.objects.filter(Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'task2.html', {'books': books})

def task3_view(request):
    books = Book.objects.filter(~Q(edition__gt=2) & ~Q(title__icontains='qu') & ~Q(author__icontains='qu'))
    return render(request, 'task3.html', {'books': books})

def task4_view(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'task4.html', {'books': books})

def task5_view(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'task5.html', {'stats': stats})

def task7_view(request):
    from django.db.models import Count
    city_stats = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'task7.html', {'city_stats': city_stats})

def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'last_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        Book.objects.create(title=title, author=author)
        return redirect('/books/lab9_part1/last_list')
    return render(request, 'add_book.html')

def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.save()
        return redirect('/books/lab9_part1/last_list')
    return render(request, 'edit_book.html', {'book': book})

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/books/lab9_part1/last_list')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            form.save_m2m()  # Save the many-to-many relationship
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to student list view
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')

def image_list(request):
    # Fetch all images from the database
    images = ImageModel.objects.all()
    return render(request, 'image_list.html', {'images': images})

def upload_image(request):
    # Handle form submission
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)  # Include the FILES parameter for handling images
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('image_list')  # Redirect to the image list after successful upload
    else:
        form = ImageForm()  # Display an empty form if the request is GET
    return render(request, 'upload_image.html', {'form': form})
    





