from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages  # Import messages framework
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import AuthorForm, BookForm
from .models import Author, Book


# Create your views here.

"""
    1. dispatch() - to determine the type of request (GET, POST, etc.)
    2. http_method_not_allowed() - to handle unsupported HTTP methods
    3. options() - to handle OPTIONS requests
"""


class Home(TemplateView):
    template_name = 'book/index.html'
"""
class TemplateView(View):
    template_name = 'template_name'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context)
"""

class ListAuthor(LoginRequiredMixin, ListView):
    model = Author
    template_name = 'book/authors/list_authors.html'
    context_object_name = 'authors'
    queryset = Author.objects.filter(is_active=True)

"""
def list_authors(request):
    authors = Author.objects.filter(is_active=True)
    return render(request, 'book/list_authors.html', {'authors': authors})
"""

class EditAuthor(LoginRequiredMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'book/authors/create_author.html'
    success_url = reverse_lazy('book:list_authors')  # Redirect to the list of authors after successful edit


"""
def edit_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    
    if request.method == 'GET':
        author_form = AuthorForm(instance=author)
    else:
        author_form = AuthorForm(request.POST, instance=author)
        if author_form.is_valid():
            author_form.save()
            return redirect('book:list_authors')
        
    return render(request, 'book/create_author.html', {'author_form': author_form})
"""

class CreateAuthor(LoginRequiredMixin, CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'book/authors/create_author.html'
    success_url = reverse_lazy('book:list_authors')  # Redirect to the list of authors after successful creation
    
"""
def create_author(request):
    if request.method == 'POST':
        print(request.POST) # Debugging line to print POST data
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
           
            return redirect('index')
    else:
        author_form = AuthorForm()
        print(author_form)
    return render(request, 'book/create_author.html', {'author_form': author_form})
"""

class DeleteAuthor(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = 'book/authors/author_confirm_delete.html'
    success_url = reverse_lazy('book:authors:list_authors')
   

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()  # Get the object to be deleted
        # Instead of deleting the object, we set is_active to False
        self.object.is_active = False
        self.object.save()
        messages.success(request, 'Author deleted successfully.')
        return HttpResponseRedirect(self.get_success_url())

"""
def delete_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == 'POST':
        author.is_active = False
        author.save()
        return redirect('book:list_authors')
    return render(request, 'book/delete_author.html', {'author': author})
"""

class BookListView(LoginRequiredMixin, View):
    model = Book
    form_class = BookForm
    template_name = 'book/books/books_list.html'  #queryset = Book.objects.all() by default object_list
    
    
    def get_queryset(self):
        """Return the list of items for this view."""
        return self.model.objects.filter(is_active=True)

    # Return the context which is gonna be sent to the template
    def get_context_data(self, **kwargs):
        context = {}
        context['books'] = self.get_queryset()  # Add the list of books to the context
        context['form'] = self.form_class()  # Add an empty form to the context
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book created successfully.')
            return redirect('book:books_list')


class CreateBook(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/books/create_book.html'
    success_url = reverse_lazy('book:books_list')  # Redirect to the list of books after successful creation

class EditBook(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book/books/books_list.html'
    success_url = reverse_lazy('book:books_list')  # Redirect to the list of books after successful edit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(is_active=True)  # Add the list of active books to the context
        return context

class DeleteBook(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book/books/book_confirm_delete.html'
    success_url = reverse_lazy('book:books_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()  # Get the object to be deleted
        # Instead of deleting the object, we set is_active to False
        self.object.is_active = False
        self.object.save()
        messages.success(request, 'Book deleted successfully.')
        return HttpResponseRedirect(self.get_success_url())