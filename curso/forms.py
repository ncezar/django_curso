from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario', 'senha']

def clean(self):
        user = request.GET.get('usuario')
        senha = request.GET.get('senha')
        usuario_aux = Usuario.objects.get(usuario=user)
        if usuario == user:
            return self.cleaned_data
        else:
            raise forms.ValidationError("Deu ruim")
