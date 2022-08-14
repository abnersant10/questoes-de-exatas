from django.db import models
from django.contrib.auth.models import User


class Area(models.Model):

    cod_area = models.CharField(primary_key=True, max_length=45)
    nome_area = models.CharField(max_length=90)




class Curso(models.Model):

    cod_curso = models.CharField(primary_key=True, max_length=45)
    nome_curso = models.CharField(max_length=90)
    area_cod = models.ForeignKey(Area, on_delete=models.CASCADE)


class Disciplina(models.Model):

    cod_disciplina = models.CharField(primary_key=True, max_length=45)
    nome_disciplina = models.CharField(max_length=90)
    curso_cod = models.ForeignKey(Curso,on_delete=models.CASCADE)
    area_cod = models.ForeignKey(Area,on_delete=models.CASCADE)


class Assunto(models.Model):

    cod_assunto = models.CharField(primary_key=True, max_length=45)
    assunto = models.CharField(max_length=90)
    disciplina_cod = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    curso_cod = models.ForeignKey(Curso, on_delete=models.CASCADE)
    area_cod = models.ForeignKey(Area, on_delete=models.CASCADE)


class TetaUsuario(models.Model):
    teta = models.FloatField()
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, related_name='fk')
    disciplina_cod = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    assunto_cod = models.ForeignKey(Assunto, on_delete=models.CASCADE)


class Questao(models.Model):
    cod_questao = models.CharField(primary_key=True, max_length=45)
    enunciado = models.TextField()
    banca_examinadora = models.CharField(max_length=45)
    ano_divulgacao = models.CharField(max_length=45)
    area_cod = models.ForeignKey(Area, on_delete=models.CASCADE)
    curso_cod = models.ForeignKey(Curso, on_delete=models.CASCADE)
    assunto_cod = models.ForeignKey(Assunto, on_delete=models.CASCADE)


class QuestaoAlternativa(models.Model):
    A = models.TextField()
    B = models.TextField()
    C = models.TextField()
    D = models.TextField()
    E = models.TextField()
    gabarito = models.CharField(max_length=1)
    questao_cod = models.OneToOneField(Questao, on_delete=models.CASCADE)


class QuestaoParametro(models.Model):

    A = models.FloatField()
    B = models.FloatField()
    C = models.FloatField()
    D = models.FloatField(default=1)
    questao_cod = models.OneToOneField(Questao, on_delete=models.CASCADE)
