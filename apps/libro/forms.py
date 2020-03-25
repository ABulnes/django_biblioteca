from django import forms
from .models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'last_name', 'nationality', 'description']
        labels = {
            'name': 'Nombre del autor',
            'last_name': 'Apellidos del autor',
            'nationality': 'Nacionalidad del autor',
            'description': 'Biografía'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre de autor',
                    'id': 'name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese apellidos de autor',
                    'id': 'last_name'
                }
            ),
            'nationality': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nacionalidad del autor',
                    'id': 'nationality'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese descripción del autor',
                    'id': 'description'
                }
            )
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'author']
        labels = {
            'title': 'Título del Libro',
            'publication_date': 'Fecha de publicación',
            'author': 'Autor(es)'
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese título del libro',
                    'id': 'title'
                }
            ),
            'publication_date': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control',
                    'id': 'publication_date'
                }
            ),
            'author': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'id': 'author'
                }
            )
        }
