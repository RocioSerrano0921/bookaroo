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

    def get_authors(self):
        return ", ".join([author.fullname for author in self.author.all()])


class BookReservation(models.Model):
    """ Model to manage book reservations """
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'reservations')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reservations')
    days_reserved = models.PositiveIntegerField(default=7)  # Default reservation period is 7 days
    reserved_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        """ Meta data for BookReservation """
        verbose_name = "Book Reservation"
        verbose_name_plural = "Book Reservations"

    def __str__(self):
        """ Unicode Representation of BookReservation """
        return f"{self.user.username} - {self.book.title} - {self.reserved_at}"