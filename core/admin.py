from django.contrib import admin
from .models import disciplina, questao, questao_alternativa, questao_parametro, teta_usuario
# Register your models here.

class DisciplinaAdmin(admin.ModelAdmin):
    ...

class QuestaoAdmin(admin.ModelAdmin):
    ...

class QuestaoAlternativaAdmin(admin.ModelAdmin):
    ...

class QuestaoParametroAdmin(admin.ModelAdmin):
    ...

class QuestaoCaracteristicaAdmin(admin.ModelAdmin):
    ...

class TetaUsuarioAdmin(admin.ModelAdmin):
    ...

admin.site.register(disciplina, DisciplinaAdmin)
admin.site.register(questao, QuestaoAdmin)
admin.site.register(questao_alternativa, QuestaoAlternativaAdmin)
admin.site.register(questao_parametro, QuestaoParametroAdmin)
admin.site.register(teta_usuario, TetaUsuarioAdmin)
