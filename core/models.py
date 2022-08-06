from django.db import models
from django.contrib.auth.models import User
from django.forms import BooleanField, CharField, ChoiceField, DateField, EmailField, FloatField, IntegerField

# Create your models here.

class disciplina(models.Model):
    cod_d = models.AutoField(auto_created = True,
                  primary_key = True,
                  serialize = False, 
                  verbose_name ='ID'
                )
    area = models.CharField(max_length=45)
    curso = models.CharField(max_length=45)
    nome = models.CharField(max_length=45)
    assunto = models.CharField(max_length=45)
    especialidade = models.CharField(max_length=45)

class questao(models.Model):
    cod_q = models.AutoField(auto_created = True,
                  primary_key = True,
                  serialize = False, 
                  verbose_name ='ID'
                )
    enunciado = models.TextField()
    banca = models.CharField(max_length=45)
    ano = models.CharField(max_length=45)

    def __str__(self):
        return str(self.cod_q)

class questao_alternativa(models.Model):
    cod_qa = models.OneToOneField(questao, on_delete=models.CASCADE)
    a = models.TextField()
    b = models.TextField()
    c = models.TextField()
    d = models.TextField()
    e = models.TextField()
    gabarito = models.CharField(max_length=1)
    
class questao_parametro(models.Model):
    cod_qp = models.OneToOneField(questao, on_delete=models.CASCADE)
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()

    def __str__(self):
        return str(self.cod_qp)


class teta_usuario(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, related_name='fk')
    curso = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=100)
    assunto = models.CharField(max_length=100)
    teta = models.FloatField()

    def __str__(self):
        return str(self.usuario)
