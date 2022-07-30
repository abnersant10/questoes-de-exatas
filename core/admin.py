from django.contrib import admin
from .models import questao, questao_catacteristica, questao_parametro, teta_usuario
# Register your models here.


class QuestaoAdmin(admin.ModelAdmin):
    ...

class QuestaoParametroAdmin(admin.ModelAdmin):
    ...

class QuestaoCaracteristicaAdmin(admin.ModelAdmin):
    ...

class TetaUsuarioAdmin(admin.ModelAdmin):
    ...


admin.site.register(questao, QuestaoAdmin)
admin.site.register(questao_parametro, QuestaoParametroAdmin)
admin.site.register(questao_catacteristica, QuestaoCaracteristicaAdmin)
admin.site.register(teta_usuario, TetaUsuarioAdmin)
