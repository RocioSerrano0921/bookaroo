from django.test import TestCase
from django.contrib.auth.models import User
from apps.book.models import Book, BookReservation
from apps.book.forms import EditDaysReservationForm

class EditDaysReservationFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.book = Book.objects.create(
            title="Test Book",
            published_date="2025-01-01",
            stock=5,
            is_active=True
        )
        self.reservation = BookReservation.objects.create(
            user=self.user,
            book=self.book,
            days_reserved=7,
            is_active=True
        )

    def test_edit_days_reservation_valid(self):
        form = EditDaysReservationForm(instance=self.reservation, data={'days_reserved': 10})
        self.assertTrue(form.is_valid())
        updated_reservation = form.save()
        self.assertEqual(updated_reservation.days_reserved, 10)

    def test_edit_days_reservation_too_low(self):
        form = EditDaysReservationForm(instance=self.reservation, data={'days_reserved': 0})
        self.assertFalse(form.is_valid())
        self.assertIn('days_reserved', form.errors)

    def test_edit_days_reservation_too_high(self):
        form = EditDaysReservationForm(instance=self.reservation, data={'days_reserved': 20})
        self.assertFalse(form.is_valid())
        self.assertIn('days_reserved', form.errors)
