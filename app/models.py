from django.db import models

class AuthorContainer(models.Model):
    created_on = models.DateField(auto_now=True, null=True)


class Author(models.Model):
    author_container = models.ForeignKey(AuthorContainer, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)
    isbn = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title