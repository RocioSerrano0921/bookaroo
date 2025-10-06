from django import forms
from .models import Author, Book, BookReservation

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'country']
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
        }


class BookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.filter(is_active=True)
        
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'description', 'stock', 'image']
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
        }