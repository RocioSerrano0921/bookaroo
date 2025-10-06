from django.urls import path
from .views import *

urlpatterns = [
    path('authors/create_author/', CreateAuthor.as_view(), name='create_author'),
    path('authors/list_authors/', ListAuthor.as_view(), name='list_authors'),
    path('authors/edit_author/<int:pk>/', EditAuthor.as_view(), name='edit_author'),
    path('authors/delete_author/<int:pk>/', DeleteAuthor.as_view(), name='delete_author'),

    path('books/book/', BookListView.as_view(), name='books_list'),  # New URL pattern for books list view
    path('books/create_book/', CreateBook.as_view(), name='create_book'),
    path('books/edit_book/<int:pk>/', EditBook.as_view(), name='edit_book'),
    path('books/delete_book/<int:pk>/', DeleteBook.as_view(), name='delete_book'),
    #General URLs
    path('books/available-books-list/', AvailableBooksView.as_view(), name='available_books_list'),  # New URL pattern for available books view
    path('books/book-detail/<int:pk>/', AvailablelBookDetail.as_view(), name='book_detail'),  # New URL pattern for book detail view
    path('books/reserve-book/<int:pk>/', RegisterBookReservation.as_view(), name='reserve_book'),  # New URL pattern for reserving a book
]
