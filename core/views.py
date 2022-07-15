from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import *

# Create your views here.


def home(request):
    # se usuário esta autenticado vá para pagina inicial ####
    if request.method == 'POST':
        email = str(request.POST.get('email'))
        senha = request.POST.get('senha')
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect("pagina-inicial")
    if request.user.is_authenticated:
        return redirect("pagina-inicial")
    else:
        # username ou senha incorreta
        return render(request, "index.html")


def logout_view(request):
    logout(request)
    return redirect('/')


def cadastro(request):
    return render(request, 'cadastro.html')


def pag_inicial(request):
    return render(request, 'pagina-inicial.html')
