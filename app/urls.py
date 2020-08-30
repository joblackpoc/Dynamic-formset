from django.urls import path
from .views import author_books_formset

urlpatterns = [
    path('',author_books_formset,name='index'),
]