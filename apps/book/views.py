from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages  # Import messages framework
from django.http import HttpResponse
from .forms import AuthorForm
from .models import Author

# Create your views here.


def index(request):
    return render(request, 'book/index.html')


def create_author(request):
    if request.method == 'POST':
        print(request.POST) # Debugging line to print POST data
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            # messages.add_message(
            #     request, messages.SUCCESS,
            #     "Your author has been created successfully."
            # )
            return redirect('index')
    else:
        author_form = AuthorForm()
        print(author_form)
    return render(request, 'book/create_author.html', {'author_form': author_form})


def list_authors(request):
    authors = Author.objects.filter(is_active=True)
    return render(request, 'book/list_authors.html', {'authors': authors})


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


def delete_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == 'POST':
        author.is_active = False
        author.save()
        return redirect('book:list_authors')
    return render(request, 'book/delete_author.html', {'author': author})