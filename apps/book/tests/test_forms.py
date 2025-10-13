from django.test import TestCase
from django.contrib.auth.models import User
from apps.book.models import Book, BookReservation
from apps.book.forms import BookReservationForm, EditDaysReservationForm  # <-- IMPORT NECESARIO


class BookReservationFormTest(TestCase):
    def setUp(self):
        # Crear usuario
        self.user = User.objects.create_user(username='testuser', password='12345')
        
        # Crear libro con stock suficiente
        self.book = Book.objects.create(
            title="Test Book",
            published_date="2025-01-01",
            stock=5,  
            is_active=True
        )

    def test_create_reservation_valid(self):
    # Pasa data vacío para que Django considere el form bound
        form = BookReservationForm(user=self.user, book=self.book, data={})
        self.assertTrue(form.is_valid())  # Ahora sí debería pasar
        reservation = form.save()
        self.assertEqual(reservation.book.stock, 5)
        self.assertEqual(reservation.user, self.user)

