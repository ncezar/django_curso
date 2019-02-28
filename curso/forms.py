from django import forms
from .models import Usuario
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario', 'senha']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
