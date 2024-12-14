from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


'''
urlpatterns = [
    path('', views.index1, name='index1'),
    path('', views.index),
    path('index2/<int:val1>/', views.index2)

    
]'''
urlpatterns = [
    path('', views.index),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>', views.viewbook)
]
urlpatterns = [
    path('', views.index5, name= "books.index5"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('books/', views.one_book, name="books.one_book"),
    path('html5/table/', views.table, name='table'),
    path('html5/formatting/', views.format, name='format'),
    path('html5/listing/', views.list, name='list'),
    path('html5/links/', views.html5_links, name='html5_links'),
    path('search/', views.search , name='search'),
    path('query/', views.query,name='query'),
    path('filter/', views.complex_query,name='filter'),
    path('task1', views.task1_view, name='task1'),
    path('task2', views.task2_view, name='task2'),
    path('task3', views.task3_view, name='task3'),
    path('task4', views.task4_view, name='task4'),
    path('task5', views.task5_view, name='task5'),
    path('task7', views.task7_view, name='task7'),
    path('lab9_part1/last_list', views.list_books, name='list_books'),
    path('lab9_part1/addbook', views.add_book, name='add_book'),
    path('lab9_part1/editbook/<int:id>', views.edit_book, name='edit_book'),
    path('lab9_part1/deletebook/<int:id>', views.delete_book, name='delete_book'),
    
    path('studentlist/', views.student_list, name='student_list'),
    path('add/', views.student_add, name='student_add'),
    path('update/<int:pk>/', views.student_update, name='student_update'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),

    path('upload/', views.upload_image, name='upload_image'),
    path('images/', views.image_list, name='image_list'),





     
 
    



    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


