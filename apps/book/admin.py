from django.contrib import admin
from .models import Author, Book, BookReservation

# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookReservation)