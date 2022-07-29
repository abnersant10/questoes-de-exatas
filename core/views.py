from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import *
from django.contrib.auth.models import User

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
    if request.method == 'POST':
        nome = str(request.POST.get('nome'))
        sobrenome = str(request.POST.get('sobrenome'))
        email = str(request.POST.get('email'))
        senha = str(request.POST.get('senha'))
        User.objects.create_user(
            username=email, first_name=nome, last_name=sobrenome, password=senha)

    return render(request, 'cadastro.html')


def pag_inicial(request):
    return render(request, 'pagina-inicial.html')

def consultar_questoes(request):
    return render(request, 'consultar-questoes.html')
