from django.shortcuts import render
from .forms import UsuarioForm
from .forms import Usuario
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def base(request):
    return render(request, "curso/base.html")

def entrar(request):
    return render(request, "curso/login.html")

def cadastro(request):
    if request.method=='POST':
        form = UsuarioForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioForm()
    context = {'form': form}
    return render(request, "curso/cadastro.html", context)
