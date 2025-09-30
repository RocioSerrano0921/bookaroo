from django.urls import path
from .views import CreateAuthor, ListAuthor, EditAuthor, DeleteAuthor

urlpatterns = [
    path('create_author/', CreateAuthor.as_view(), name='create_author'),
    path('list_authors/', ListAuthor.as_view(), name='list_authors'),
    path('edit_author/<int:pk>/', EditAuthor.as_view(), name='edit_author'),
    path('delete_author/<int:pk>/', DeleteAuthor.as_view(), name='delete_author'),
]
