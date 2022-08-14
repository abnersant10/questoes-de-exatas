from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import *
from django.contrib.auth.models import User
from .models import Questao
import json
import pathlib

def home(request):

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


def consultar_quest(request):

    folder = json.load(
        open(str(pathlib.Path().resolve())+'\\base\\folder.json', encoding='utf8'))
    context = {
        "folder": folder,
    }
    return render(request, 'consultar.html', context)


def nav_quest(request, assunto, disciplina):
    itens = Questao.objects.all()
    paginator = Paginator(itens, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    assunto = 'assunto'
    disciplina = 'disciplina'
    context = {
        'assunto' : assunto,
        'disciplina': disciplina,
    }
    return render(request, 'nav-quest.html', context)