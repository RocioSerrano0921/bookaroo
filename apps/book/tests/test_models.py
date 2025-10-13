from django.test import TestCase
from apps.book.models import Book, Author
from datetime import date

class BookModelTest(TestCase):
    
    def setUp(self):
        # Crear un autor de ejemplo
        self.author = Author.objects.create(
            first_name="John",
            last_name="Doe",
            country="USA"
        )
        # Crear un libro sin asignar autor directamente
        self.book = Book.objects.create(
            title="Python 101",
            published_date=date.today(),
            stock=5
        )
        # Asignar el autor usando .set()
        self.book.author.set([self.author])

    def test_book_creation(self):
        # Verificar que el libro se creó correctamente
        self.assertEqual(self.book.title, "Python 101")
        self.assertEqual(self.book.stock, 5)
        self.assertEqual(self.book.author.count(), 1)
        self.assertEqual(self.book.author.first().first_name, "John")
        self.assertEqual(self.book.author.first().last_name, "Doe")

    def test_book_stock_decrement(self):
        # Simular que se toma una copia y verificar stock
        self.book.stock -= 1
        self.book.save()
        self.book.refresh_from_db()
        self.assertEqual(self.book.stock, 4)
