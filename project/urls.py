from django.contrib import admin
from django.urls import path, include
import bookmodule.views
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('page.urls')),
    
    path('', bookmodule.views.index),
    path('books/',include('bookmodule.urls') ),
    path('index2/<int:val1>/', bookmodule.views.index2)
    

]'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include("bookmodule.urls")), #include urls.py of bookmodule app
    path('users/', include("usermodule.urls")) , #include urls.py of usermodule app
    path('pages/', include("pages.urls")),
    path('page/', include("page.urls"))
]
