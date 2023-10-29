from django.db import models
from django.forms import ModelForm
from django.utils.text import slugify


class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    book_name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    publisher = models.CharField(max_length=50)
    published_date = models.DateField()
    author = models.CharField(max_length=50)
    cover = models.CharField(max_length=50)
    slug = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.book_name)
        super(Book, self).save(*args, **kwargs)
