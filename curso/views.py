from django.shortcuts import render
from .forms import UserForm
from .forms import Usuario
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def base(request):
    return render(request, "curso/base.html")

def logado(request):
    return render(request, "curso/logado.html")

def cadastro(request):
    if request.method=='POST':
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    else:
        form = UserForm()
    context = {'form': form}
    return render(request, "curso/cadastro.html", context)
