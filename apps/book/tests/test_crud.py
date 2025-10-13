from django.test import TestCase
from apps.book.models import Author, Book
from datetime import date

class AuthorCRUDTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(
            first_name="John",
            last_name="Doe",
            country="USA",
            is_active=True
        )

    def test_create_author(self):
        self.assertEqual(self.author.first_name, "John")
        self.assertEqual(self.author.last_name, "Doe")
        self.assertTrue(self.author.is_active)

    def test_read_author(self):
        author = Author.objects.get(id=self.author.id)
        self.assertEqual(author.fullname, "John Doe")

    def test_update_author(self):
        self.author.first_name = "Jane"
        self.author.save()
        updated_author = Author.objects.get(id=self.author.id)
        self.assertEqual(updated_author.first_name, "Jane")

    def test_delete_author(self):
        author_id = self.author.id
        self.author.delete()
        with self.assertRaises(Author.DoesNotExist):
            Author.objects.get(id=author_id)


class BookCRUDTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(
            first_name="John",
            last_name="Doe",
            country="USA",
            is_active=True
        )
        self.book = Book.objects.create(
            title="Sample Book",
            published_date=date.today(),
            stock=5,
            is_active=True
        )
        self.book.author.add(self.author)

    def test_create_book(self):
        self.assertEqual(self.book.title, "Sample Book")
        self.assertEqual(self.book.stock, 5)
        self.assertIn(self.author, self.book.author.all())

    def test_read_book(self):
        book = Book.objects.get(id=self.book.id)
        self.assertEqual(book.get_authors(), "John Doe")

    def test_update_book(self):
        self.book.title = "Updated Book"
        self.book.stock = 10
        self.book.save()
        updated_book = Book.objects.get(id=self.book.id)
        self.assertEqual(updated_book.title, "Updated Book")
        self.assertEqual(updated_book.stock, 10)

    def test_delete_book(self):
        book_id = self.book.id
        self.book.delete()
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(id=book_id)
