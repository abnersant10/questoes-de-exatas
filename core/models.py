from django.db import models
from django.contrib.auth.models import User
from django.forms import BooleanField, CharField, ChoiceField, DateField, EmailField, FloatField, IntegerField

# Create your models here.

class questao(models.Model):
    cod_q = models.AutoField(primary_key=True)
    enunciado = models.TextField()
    alt_a = models.TextField()
    alt_b = models.TextField()
    alt_c = models.TextField()
    alt_d = models.TextField()
    alt_e = models.TextField()
    gabarito = models.CharField(max_length=1)

    def __str__(self):
        return str(self.cod)

class questao_parametro(models.Model):
    cod_qp = models.OneToOneField(questao, on_delete=models.CASCADE)
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()

class questao_catacteristica(models.Model):
    cod_qc = models.ForeignKey(questao, on_delete=models.CASCADE, default=None, related_name='fk')
    curso = models.CharField(max_length=45)
    banca = models.CharField(max_length=45)
    disciplina = models.CharField(max_length=45)
    assunto = models.CharField(max_length=45)
    ano = models.IntegerField()



class teta_usuario(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, related_name='fk')
    curso = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=100)
    assunto = models.CharField(max_length=100)
    teta = models.FloatField()

    def __str__(self):
        return str(self.usuario)
