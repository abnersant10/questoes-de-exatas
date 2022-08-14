from django.contrib import admin
from .models import *


class AreaAdmin(admin.ModelAdmin):

    list_display = ('nome_area','cod_area')


class CursoAdmin(admin.ModelAdmin):

    list_display = ('nome_curso', 'cod_curso', 'area_cod')


class DisciplinaAdmin(admin.ModelAdmin):

    list_display = ('nome_disciplina', 'cod_disciplina', 'curso_cod', 'area_cod')


class AssuntoAdmin(admin.ModelAdmin):

    list_display = ('assunto', 'cod_assunto', 'disciplina_cod', 'curso_cod', 'area_cod')


class TetaUsuarioAdmin(admin.ModelAdmin):

    list_display = ('usuario', 'teta', 'disciplina_cod', 'assunto_cod')


class QuestaoAdmin(admin.ModelAdmin):

    list_display = ('cod_questao', 'enunciado', 'banca_examinadora', 'ano_divulgacao', 'curso_cod', 'assunto_cod')


class QuestaoAlternativaAdmin(admin.ModelAdmin):

    list_display = ('questao_cod', 'A', 'B', 'C', 'D', 'E', 'gabarito')


class QuestaoParametroAdmin(admin.ModelAdmin):

    list_display = ('questao_cod', 'A', 'B', 'C','D')


admin.site.register(Area, AreaAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Assunto, AssuntoAdmin)
admin.site.register(TetaUsuario, TetaUsuarioAdmin)
admin.site.register(Questao, QuestaoAdmin)
admin.site.register(QuestaoAlternativa, QuestaoAlternativaAdmin)
admin.site.register(QuestaoParametro, QuestaoParametroAdmin)
