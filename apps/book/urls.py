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
]
