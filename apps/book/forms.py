from django import forms
from .models import Author, Book, BookReservation


class BookReservationForm(forms.ModelForm):
    """
    Form to handle book reservations and ensure user and book are set into
    self.instance before form.is_valid and that way clean() 
    have their values to validate.

    """
    class Meta:
        model = BookReservation
        fields = []  # No fields to fill in the form, as user and book are set in the view

    def __init__(self, *args, user=None, book=None, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the user and book for the reservation
        if user is not None:
            self.instance.user = user
        if book is not None:
            self.instance.book = book


class EditDaysReservationForm(BookReservationForm):
    """
    Form to edit only the days_reserved field of an existing BookReservation.
    """
    days_reserved = forms.IntegerField(
        label="Days to Reserve",
        min_value=3,
        max_value=15,
        help_text="You can reserve a book for 3 to 15 days."
    )

    class Meta:
        model = BookReservation
        fields = ['days_reserved']  # Just the days_reserved field to edit


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'country', 'is_active']
        # labels = {
        #     'first_name': 'Author First Name',
        #     'last_name': 'Author Last Name',
        #     'country': 'Author Nationality',
        # }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Enter first name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter last name'
                }
            ),             
            'country': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Author nationality'
                }
            ),
            'is_active': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            ),
        }


class BookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.all()
        
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'description', 'stock', 'image', 'is_active']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Enter book title'
                }
            ),
            'author': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'multiple': 'multiple',
                }
            ),             
            'published_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Enter book description',
                    'rows': 4,
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter book stock',
                }
            ),
            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'is_active': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            ),
        }