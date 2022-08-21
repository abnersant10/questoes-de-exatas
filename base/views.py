from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import *
from django.contrib.auth.models import User
from .models import Assunto, Disciplina, Questao, QuestaoAlternativa, QuestaoParametro, TetaUsuario
import json
import pathlib
from catsim.selection import UrrySelector
from catsim.estimation import NumericalSearchEstimator
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
        user = User.objects.create_user(
            username=email, first_name=nome, last_name=sobrenome, password=senha, is_staff=True)
        user.save()

    return render(request, 'cadastro.html')


def pag_inicial(request):
    if request.user.is_authenticated:
        frist_name = request.user.first_name
        print(frist_name)
        context = {
            "frist_name": frist_name,
        }
        return render(request, 'pagina-inicial.html', context)
    else:
        return redirect('home')


def consultar_quest(request):

    folder = json.load(
        open(str(pathlib.Path().resolve()) + '\\base\\folder.json', encoding='utf8'))
    context = {
        "folder": folder,
    }
    return render(request, 'consultar.html', context)


def nav_quest(request, assunto, disciplina, ):
    if request.user.is_authenticated:
        # BUSCA
        cod_assunto = Assunto(cod_assunto='CE01CCAS01')
        cod_disciplina = Disciplina(cod_disciplina='A01CCDS01')
        disciplina = disciplina.replace('-', ' ')
        assunto = assunto.replace('-', ' ')
        disciplina_select = Disciplina.objects.filter(nome_disciplina__contains=disciplina)
        assunto_select = Assunto.objects.filter(assunto__contains=assunto)
        itens_select = Questao.objects.filter(assunto_cod=cod_assunto)
        tot_itens = len(itens_select)
        interval_est = 2
        teta_usuario = TetaUsuario.objects.filter(assunto_cod=cod_assunto)
        teta = 0
        if teta_usuario.count() == 0:
            email = User.objects.get(username=request.user.username)
            novo_teta_usuario = TetaUsuario.objects.create(teta=0.0, usuario=email, disciplina_cod=cod_disciplina,
                                                           assunto_cod=cod_assunto)
            novo_teta_usuario.save()

        for i in teta_usuario:
            teta = i.teta

        vetor_param = []

        for item in itens_select:
            a = QuestaoParametro.objects.get(questao_cod=item.cod_questao).A
            b = QuestaoParametro.objects.get(questao_cod=item.cod_questao).B
            c = QuestaoParametro.objects.get(questao_cod=item.cod_questao).C
            d = QuestaoParametro.objects.get(questao_cod=item.cod_questao).D
            param_i = [a, b, c, d]
            vetor_param.append(param_i)

        vetor_param = array(vetor_param)

        item = UrrySelector()
        itens_usados = request.POST.get('id_itens')

        if itens_usados is None:
            itens_usados = ''
        itens_usados = [int(i) for i in itens_usados.split()]

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
        itens_usados.append(i_novo_item)

        server_id_items = request.POST.get('server_id_items')

        if server_id_items is None:
            server_id_items = ''

        if len(itens_usados) < tot_itens:
            itens_usados = " ".join(map(str, itens_usados))
            server_id_items = itens_usados + ' '
        # receber e tratar os dados do vetor respostas
        user_resp = request.POST.get('user_resp')
        server_vet_resp = request.POST.get('vet_resp')
        if server_vet_resp is None:
            server_vet_resp = ''
        if user_resp == gabarito:
            server_vet_resp = server_vet_resp + '1'
        elif user_resp is not None:
            server_vet_resp = server_vet_resp + '0'

        if isinstance(itens_usados, list):
            return HttpResponse("Não há mais questões disponíveis")
        else:
            itens_usados = [int(i) for i in itens_usados.split()]

        cliente_est = request.POST.get('cli_est')
        if cliente_est is None:
            cliente_est = 0
        if int(cliente_est) >= 0:
            cliente_est = int(cliente_est) + 1
        print(cliente_est, '==', interval_est)
        if int(cliente_est)  == interval_est:
            # estimar o novo teta

            vet_resp = []
            for i in server_vet_resp:
                if i == '1':
                    vet_resp.append(True)
                else:
                    vet_resp.append(False)

            items_administrados = [int(i) for i in server_id_items.split()]
            items_administrados.pop()
            log_likelihood = NumericalSearchEstimator()
            print("itens administrados:", itens_usados)
            print("vetor de resposta:", vet_resp)
            novo_teta = NumericalSearchEstimator.estimate(log_likelihood, items=vetor_param,
                                                          administered_items=itens_usados, response_vector=vet_resp,
                                                          est_theta=teta)

            email = User.objects.get(username=request.user.username)
            novo_teta_usuario = TetaUsuario.objects.create(teta=novo_teta, usuario=email, disciplina_cod=cod_disciplina,
                                                           assunto_cod=cod_assunto)
            novo_teta_usuario.save()
            cliente_est = 0

        # a cada 5 questões zerar
        context = {
            'assunto': assunto_select,
            'disciplina': disciplina_select,
            'itens_selec': itens_select,
            'enunciado': enunciado,
            'ano': ano,
            'banca': banca,
            'alt_a': alt_a,
            'alt_b': alt_b,
            'alt_c': alt_c,
            'alt_d': alt_d,
            'alt_e': alt_e,
            'gabarito': gabarito,
            'param_a': param_a,
            'param_b': param_b,
            'param_c': param_c,
            'teta': teta,
            'server_vet_resp': server_vet_resp,
            'server_id_items': server_id_items,
            'server_cli_est': cliente_est,

        }
        return render(request, 'nav-quest.html', context)
    else:
        return redirect('home')
