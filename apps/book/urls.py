from django.urls import path
from .views import create_author, delete_author, list_authors, edit_author

urlpatterns = [
    path('create_author/', create_author, name='create_author'),
    path('list_authors/', list_authors, name='list_authors'),
    path('edit_author/<int:author_id>/', edit_author, name='edit_author'),
    path('delete_author/<int:author_id>/', delete_author, name='delete_author'),
]
