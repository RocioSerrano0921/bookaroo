from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages  # Import messages framework
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView, View, ListView, UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.db import transaction
from django.utils import timezone
from django.db import models
from datetime import timedelta
from .forms import AuthorForm, BookForm, BookReservationForm, EditDaysReservationForm
from .models import Author, Book, BookReservation


# Create your views here.

"""
    1. dispatch() - to determine the type of request (GET, POST, etc.)
    2. http_method_not_allowed() - to handle unsupported HTTP methods
    3. options() - to handle OPTIONS requests
"""


class Home(TemplateView):
    template_name = 'book/index.html'


class ListAuthor(LoginRequiredMixin, ListView):
    model = Author
    template_name = 'book/authors/list_authors.html'
    context_object_name = 'authors'
    queryset = Author.objects.filter(is_active=True)



class EditAuthor(LoginRequiredMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'book/authors/create_author.html'
    success_url = reverse_lazy('book:list_authors')  # Redirect to the list of authors after successful edit



class CreateAuthor(LoginRequiredMixin, CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'book/authors/create_author.html'
    success_url = reverse_lazy('book:list_authors')  # Redirect to the list of authors after successful creation
    

class DeleteAuthor(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = 'book/authors/author_confirm_delete.html'
    success_url = reverse_lazy('book:list_authors')
   
    def form_valid(self, form):
        # Soft Delete - Instead of deleting, deactivate
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save(update_fields=['is_active'])
        messages.success(self.request, 'Author deleted successfully.')
        return HttpResponseRedirect(self.get_success_url())


class BookListView(LoginRequiredMixin, View):
    model = Book
    form_class = BookForm
    template_name = 'book/books/books_list.html' 
    
    
    def get_queryset(self):
        """Return the list of items for this view."""
        return self.model.objects.filter(is_active=True)

    # Return the context which is gonna be sent to the template
    def get_context_data(self, **kwargs):
        """
        Get the context for the template, including the list of books and an empty form for creating a new book.
        """
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
    template_name = 'book/books/create_book.html'
    success_url = reverse_lazy('book:books_list')  # Redirect to the list of books after successful edit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(is_active=True)  # Add the list of active books to the context
        return context

class DeleteBook(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book/books/book_confirm_delete.html'
    success_url = reverse_lazy('book:books_list')

    def form_valid(self, form):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save(update_fields=['is_active'])
        messages.success(self.request, 'Book deleted successfully.')
        return HttpResponseRedirect(self.get_success_url())
    
    

class AvailableBooksView(LoginRequiredMixin, ListView):
    model = Book
    paginate_by = 6  # Number of books per page
    template_name = 'book/books/available_books.html'
    
    def get_queryset(self):
        """Return the list of available books (stock > 0)."""
        queryset = self.model.objects.filter(is_active=True, stock__gte=1)
        return queryset
    
class AvailablelBookDetail(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'book/books/available_book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs) # Get the existing context data
        book = self.get_object()  # Get the current book object
        has_active = BookReservation.objects.filter(user=self.request.user, book=book, is_active=True).exists()
        ctx['can_reserve'] = book.is_active and book.stock > 0 and not has_active
        return ctx


class RegisterBookReservation(LoginRequiredMixin, CreateView):
    """View to register a book reservation"""
    model = BookReservation
    form_class = BookReservationForm
    success_url = reverse_lazy('book:available_books_list')

    def dispatch(self, request, *args, **kwargs):
        self.book = get_object_or_404(Book, pk=kwargs["pk"])
        if request.method == "GET":
            return redirect("book:available_book_detail", pk=self.book.pk)
        return super().dispatch(request, *args, **kwargs)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        kwargs["book"] = get_object_or_404(Book, pk=self.kwargs["pk"])
        return kwargs
    
    
    def form_valid(self, form):
        with transaction.atomic():
            # 1. Lock the book record for this transaction
            book = Book.objects.select_for_update().get(pk=self.book.pk)

            # 2. Prevent duplicate active reservation
            # 2.1 Check if the user already has an active reservation for this book
            if BookReservation.objects.filter(user=self.request.user, book=book, is_active=True).exists():
                messages.warning(self.request, "You already have an active reservation for this book.")
                return redirect('success_url')

            # 2.2 Double-check book availability
            if not book.is_active or book.stock < 1:
                messages.error(self.request, "Sorry, this book is not available right now.")
                return redirect('success_url')
            # 4. Create the reservation
            form.instance.user = self.request.user
            form.instance.book = book
            response = super().form_valid(form)
           

            # book.stock : we decrease stock with signals (models.py)
            messages.success(self.request, f'You have successfully reserved "{book.title}".')
            return response


# To show resarvations of the logged-in user
class MyReservationsView(LoginRequiredMixin, ListView):
    """
    View that shows all reservations for the logged-in user"""
    model = BookReservation
    template_name = 'book/books/my_reservations.html'
    context_object_name = 'reservations'
    paginate_by = 6  # Number of reservations per page

    def get_queryset(self):
        """Return the list of reservations for the logged-in user."""
        reservations = BookReservation.objects.filter(user=self.request.user)
        for r in reservations:
            r.expires_at = r.reserved_at + timezone.timedelta(days=r.days_reserved)
        return reservations
    

# To cancel a reservation
class CancelReservationView(LoginRequiredMixin, View):
    """
    View to cancel a book reservation"""
    def post(self, request, pk):
        # Get the active reservation for the logged-in user
        reservation = get_object_or_404(
            BookReservation, pk=pk, user=request.user, is_active=True
        )

        # Deactivate reservation
        reservation.is_active = False
        reservation.save(update_fields=['is_active']) #Update only the is_active field
        # Increase the book stock by 1
        Book.objects.filter(pk=reservation.book.pk).update(stock=models.F('stock') + 1)

        # Success message
        messages.success(request, f'Your reservation for "{reservation.book.title}" has been cancelled.')
        return redirect('book:my_reservations')

# View to show expired reservations
class ExpiredReservationsView(LoginRequiredMixin, ListView):
    """
    View that shows all expired reservations for the logged-in user
    """
    model = BookReservation
    template_name = 'book/books/expired_reservations.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        today = timezone.now().date()
        return BookReservation.objects.filter(
            user=self.request.user,
            expires_at__lt=today  # expired reservations
        ).order_by('-expires_at')
    
# Edit Reservation Days View
class EditReservationDaysView(LoginRequiredMixin, UpdateView):
    model = BookReservation
    form_class = EditDaysReservationForm
    template_name = 'book/books/edit_reservation_days.html'  # Temporal file to create days reservation form

    def get_object(self, queryset=None):
        # Only allow editing of the user's own active reservations
        return get_object_or_404(
            BookReservation,
            pk=self.kwargs['pk'],
            user=self.request.user,
            is_active=True
        )

    def form_valid(self, form):
        # Save only the days_reserved field
        reservation = form.instance
        reservation.days_reserved = form.cleaned_data['days_reserved']
        reservation.save(update_fields=['days_reserved'])  # Save the updated days_reserved field
        messages.success(
            self.request,
            f'Reservation period updated to {reservation.days_reserved} days for "{reservation.book.title}".'
        )
        return redirect('book:my_reservations')


        # form.save(update_fields=['days_reserved'])
        # messages.success(
        #     self.request,
        #     f'Reservation period updated to {form.instance.days_reserved} days for "{form.instance.book.title}".'
        # )
        # return redirect('book:my_reservations')