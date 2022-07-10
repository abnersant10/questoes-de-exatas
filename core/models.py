
from dataclasses import Field
from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.forms import BooleanField, CharField, ChoiceField, DateField, EmailField, FloatField

# Create your models here.


class questao(models.Model):
    cod = models.CharField(primary_key=True, max_length=50)
    curso = CharField(max_length=100)
    disciplina = CharField(max_length=100)
    assunto = CharField(max_length=100)
    ano = CharField(max_length=20)
    multidisciplinar = BooleanField()
    # parametros da TRI
    a = FloatField()
    b = FloatField()
    c = FloatField()
    enunciado = CharField(max_length=4096)
    # alternativas (A,B,C,D,E)
    alt_a = CharField(max_length=4096)
    alt_b = CharField(max_length=4096)
    alt_c = CharField(max_length=4096)
    alt_d = CharField(max_length=4096)
    alt_e = CharField(max_length=4096)
    # alternativas (Verdadeiro, Falso)
    alt_v = CharField(max_length=4096)
    alt_f = CharField(max_length=4096)
    # Qual letra é a alternativa correta
    alt_correta = CharField(max_length=1)  # Adicionar as alternativas
    solucao = CharField(max_length=4096)


class usuario_questao(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = CharField(max_length=100)
    disciplina = CharField(max_length=100)
    assunto = CharField(max_length=100)
    teta = FloatField()
