from django import forms
from .models import Author

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