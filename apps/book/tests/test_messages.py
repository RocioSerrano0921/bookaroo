from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from apps.book.models import Book, BookReservation

class ReservationMessageTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.book = Book.objects.create(title="Test Book", published_date="2025-01-01", stock=5)

    def test_reservation_create_message(self):
        response = self.client.post(reverse('book:reserve_book', kwargs={'pk': self.book.pk}))
        
        # Check that a message exists
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        # Check the actual content of the message
        self.assertIn("successfully reserved", str(messages[0]))
        self.assertEqual(messages[0].tags, 'success')


    def test_cancel_reservation_message(self):
        reservation = BookReservation.objects.create(user=self.user, book=self.book)
        response = self.client.post(reverse('book:cancel_reservation', kwargs={'pk': reservation.pk}))
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertIn("has been cancelled", str(messages[0]))
        self.assertEqual(messages[0].tags, 'success')
