from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages  # Import messages framework
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .forms import AuthorForm
from .models import Author

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

class ListAuthor(ListView):
    model:Author
    template_name = 'book/list_authors.html'
    context_object_name = 'authors'
    queryset = Author.objects.filter(is_active=True)

"""
def list_authors(request):
    authors = Author.objects.filter(is_active=True)
    return render(request, 'book/list_authors.html', {'authors': authors})
"""

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