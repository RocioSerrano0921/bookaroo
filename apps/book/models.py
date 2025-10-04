from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    country = models.CharField(max_length=100, blank=False, null=False)
    is_active = models.BooleanField(default=True)

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.fullname  
    
    class Meta:
        ordering = ['last_name', 'first_name']


class Book(models.Model):
    title = models.CharField('Title', max_length=200, blank=False, null=False)
    published_date = models.DateField('Published Date', blank=False, null=False)
    description = models.TextField('Description', blank=True, null=True)
    stock = models.PositiveIntegerField('Stock', default=1)
    image = CloudinaryField('Image', blank=True, null=True)
    author = models.ManyToManyField(Author, related_name='books')
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
