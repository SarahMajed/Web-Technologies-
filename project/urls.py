from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
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
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)