from django.shortcuts import render
from .forms import UserForm
from .forms import Usuario
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
#...

# Create your views here.

def base(request):
    return render(request, "curso/base.html")

def logado(request):
    return render(request, "curso/logado.html")

def curso(request):
    return render(request, "curso/curso.html")

def cronograma(request):
    return render(request, "curso/cronograma.html")

def perguntas(request):
    return render(request, "curso/perguntas.html")

def cadastro(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, "curso/cadastro.html", context)
