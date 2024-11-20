from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Folder, Entry


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ("name", "date")

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ("name", "date", "folder", "content")