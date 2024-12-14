from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50, default="Untitled")
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=0)
    def __str__(self):
        return f"{self.title}"

class Address(models.Model):  
    city = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.city}"
        

class Student(models.Model):  # Rename to avoid conflicts with Task 1
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address)
    
    def __str__(self):
        return self.name
    
class ImageModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    

    def __str__(self):
        return self.title



