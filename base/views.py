from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib.auth.models import User
from .models import Assunto, Disciplina, Questao, QuestaoAlternativa, QuestaoParametro
from django.http import JsonResponse
import json
import pathlib
from catsim.selection import UrrySelector
from numpy import array
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
    disciplina_select = Disciplina.objects.filter(nome_disciplina__contains=disciplina)
    assunto_select = Assunto.objects.filter(assunto__contains=assunto)
    itens_select = Questao.objects.filter(assunto_cod='CE01CCAS01')
    itens_param = []
    tot_itens = len(itens_select)
    teta = 0 # inicialmente
    itens_usados = []
    vetor_respostas = []
    vetor_param = []


    for item in itens_select:
        a = QuestaoParametro.objects.get(questao_cod=item.cod_questao).A
        b = QuestaoParametro.objects.get(questao_cod=item.cod_questao).B
        c = QuestaoParametro.objects.get(questao_cod=item.cod_questao).C
        d = QuestaoParametro.objects.get(questao_cod=item.cod_questao).D
        param_i = []
        param_i.append(a)
        param_i.append(b)
        param_i.append(c)
        param_i.append(d)
        vetor_param.append((param_i))
        #print(vetor_param)
    vetor_param = array(vetor_param)



    if tot_itens != 0:
        print(tot_itens)
        item = UrrySelector()
        i_novo_item = item.select(items=vetor_param, administered_items=itens_usados, est_theta=teta)
        banca = itens_select[int(i_novo_item)].banca_examinadora
        ano = itens_select[int(i_novo_item)].ano_divulgacao
        enunciado = itens_select[int(i_novo_item)].enunciado
        cod_questao = itens_select[int(i_novo_item)].cod_questao
        alt_a = QuestaoAlternativa.objects.get(questao_cod=cod_questao).A
        alt_b = QuestaoAlternativa.objects.get(questao_cod=cod_questao).B
        alt_c = QuestaoAlternativa.objects.get(questao_cod=cod_questao).C
        alt_d = QuestaoAlternativa.objects.get(questao_cod=cod_questao).D
        alt_e = QuestaoAlternativa.objects.get(questao_cod=cod_questao).E
        gabarito = QuestaoAlternativa.objects.get(questao_cod=cod_questao).gabarito
        param_a = QuestaoParametro.objects.get(questao_cod=cod_questao).A
        param_b = QuestaoParametro.objects.get(questao_cod=cod_questao).B
        param_c = QuestaoParametro.objects.get(questao_cod=cod_questao).C
        itens_usados.append((i_novo_item))
        tot_itens = tot_itens - 1


        #id_item_atual = 0
        #print("ID Novo item: ", i_novo_item)
        #print(itens_select[int(i_novo_item)])
        # ADMINISTRAR O ITEM I






    #for item in itens_select:
    #    print(item)
    #text = request.GET.get('button_text')
    #print("texto: ", text)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        button_text = 196251
        return JsonResponse({'button_text': button_text}, status=200)


    context = {
        'assunto' : assunto_select,
        'disciplina': disciplina_select,
        'itens_selec' : itens_select,
        'enunciado' : enunciado,
        'ano':ano,
        'banca': banca,
        'alt_a' : alt_a,
        'alt_b': alt_b,
        'alt_c': alt_c,
        'alt_d': alt_d,
        'alt_e': alt_e,
        'gabarito' : gabarito,
        'param_a' : param_a,
        'param_b': param_b,
        'param_c': param_c,
        'teta': teta,
    }
    return render(request, 'nav-quest.html', context)