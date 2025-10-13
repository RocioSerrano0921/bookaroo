from django.test import TestCase
from django.db import models

from django.contrib.auth.models import User
from apps.book.models import Book, Author, BookReservation
from datetime import date

class BookReservationCRUDTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='12345')
        self.author = Author.objects.create(first_name='Jane', last_name='Smith', country='UK')
        self.book = Book.objects.create(title='Django Testing', published_date=date.today(), stock=3)
        self.book.author.add(self.author)

    def test_create_reservation(self):
        reservation = BookReservation.objects.create(user=self.user, book=self.book)
        self.assertEqual(reservation.is_active, True)
        self.book.refresh_from_db()
        self.assertEqual(self.book.stock, 2)  # stock decreased by post_save

    def test_cancel_reservation(self):
        reservation = BookReservation.objects.create(user=self.user, book=self.book)
        # Cancel reservation (like in your view)
        reservation.is_active = False
        reservation.save(update_fields=['is_active'])
        Book.objects.filter(pk=reservation.book.pk).update(stock=models.F('stock') + 1)

        self.book.refresh_from_db()
        self.assertEqual(self.book.stock, 3)  # Stock restored to initial value
        reservation.refresh_from_db()
        self.assertFalse(reservation.is_active)
