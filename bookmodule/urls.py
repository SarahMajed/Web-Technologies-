from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.index1, name='index1')
]