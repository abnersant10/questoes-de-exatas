from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib.auth.models import User
from .models import Assunto, Disciplina
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


def nav_quest(request, assunto,disciplina,):

    disciplina = disciplina.replace('-', ' ')
    assunto = assunto.replace('-', ' ')
    disciplina_selec = Disciplina.objects.get(nome_disciplina__contains=disciplina)
    assunto_selec = Assunto.objects.get(assunto__contains=assunto)



    context = {
        'assunto' : assunto_selec,
        'disciplina': disciplina_selec,
    }
    return render(request, 'nav-quest.html', context)