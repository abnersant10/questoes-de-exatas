from django.db import models
from django.forms import BooleanField, CharField, ChoiceField, DateField, EmailField, FloatField

# Create your models here.


class usuario(models.Model):
    nome = CharField(max_length=100)
    sobrenome = CharField(max_length=100)
    email = EmailField()
    nascimento = DateField()
    genero = CharField(max_length=50)
    perfil = CharField(max_length=50)
    teta = FloatField()


class questao(models.Model):
    nome = CharField(max_length=100)
    curso = CharField(max_length=100)
    disciplina = CharField(max_length=100)
    assunto = CharField(max_length=100)
    ano = CharField(max_length=20)
    multidisciplinar = BooleanField()
    a = FloatField()
    b = FloatField()
    c = FloatField()
    enunciado = CharField(max_length=4096)
    alternativas = ChoiceField()  # Adicionar as alternativas
    solucao = CharField(max_length=4096)
