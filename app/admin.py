from django.contrib import admin
from .models import Author,AuthorContainer,Book

admin.site.register(AuthorContainer)
admin.site.register(Author)
admin.site.register(Book)
