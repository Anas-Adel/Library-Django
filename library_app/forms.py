from django import forms
from django.forms import ModelForm 
from .models import Book

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_superuser']
        # widget = {
        #     'username' : class:
        # }


class addBook_form(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'Author', 'category','description']

        
        # def clean(self):
        #     cleaned = self.cleaned_data
        #     name = self.get('name')
        #     for instance in Book.objects.all():
        #         if instance.name == name:
        #             # raise forms.ValidationError('Book name already exist')
        #             return False
        #     return True

        # widget = {
        #     'name': forms.TextInput(attrs={})

        # }


