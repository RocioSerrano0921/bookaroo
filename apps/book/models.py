from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)  
    last_name = models.CharField(max_length=100, blank=False, null=False)
    country = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
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
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['title']
        constraints = [
            models.CheckConstraint(
                check=Q(stock__gte=0),
                name="book_stock_non_negative",
            ),
        ]
        """ constraints to ensure stock is non-negative """

    def __str__(self):
        return self.title

    def get_authors(self):
        return ", ".join([author.fullname for author in self.author.all()])


class BookReservation(models.Model):
    """ Model to manage book reservations """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'reservations')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reservations')
    days_reserved = models.PositiveIntegerField(default=7)  # Default reservation, period is 7 days
    reserved_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    is_active = models.BooleanField(default=True)
     
    def clean(self):
        super().clean()
        # Validar stock solo al crear una reserva nueva
        if self.is_active and self._state.adding:  # `_state.adding=True` -> creación
            if self.book.stock < 1:
                raise ValidationError("No stock available for this book.")

    # def clean(self):
    #     super().clean()
    #     if not self.book.is_active:
    #         if self.book.stock < 1:
    #             raise ValidationError("No stock available for this book.")
        
    def save(self, *args, **kwargs):
        self.full_clean()  # Ensure validations are checked before saving
        return super().save(*args, **kwargs)

    class Meta:
        """ Meta data for BookReservation """
        verbose_name = "Book Reservation"
        verbose_name_plural = "Book Reservations"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "book"],
                condition=Q(is_active=True),
                name="unique_active_reservation_per_user_book",
            ),
        ]
        """ Ensure a user can have only one active reservation per book """
        

    def __str__(self):
        """ Unicode Representation of BookReservation """
        return f"{self.user.username} - {self.book.title} - {self.reserved_at}"
    

def delete_author_books_relationship(sender, instance, **kwargs):
    """ Signal to handle the many-to-many relationship between Author and Book when an Author is deleted """
    if instance.is_active == False:
        author = instance.id
        books = Book.objects.filter(author__id=author)
        for book in books:
            book.author.remove(author)



 
# Adjust book stock on reservation cancellation
@receiver(post_save, sender=BookReservation)
def decrease_book_stock_on_new_reservation(sender, instance, created, **kwargs):
    """
    Decrease the stock of the book by 1 when a new active reservation is created.
    """
    if created and instance.is_active:
        # Decrease stock using F() to avoid race conditions
        Book.objects.filter(pk=instance.book.pk).update(stock=models.F('stock') - 1)


# @receiver(post_delete, sender=BookReservation)
# def increase_book_stock(sender, instance, **kwargs):
#     """Increase the book's stock when a reservation is deleted or canceled."""
#     Book.objects.filter(pk=instance.book.pk).update(stock=models.F('stock') + 1)

post_save.connect(delete_author_books_relationship, sender=Author)
