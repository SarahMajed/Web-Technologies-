from django.contrib import admin
from .models import Book
from .models import Address, Student,ImageModel
# Register your models here.
admin.site.register(Book)
admin.site.register(Address)
admin.site.register(Student)
admin.site.register(ImageModel)
