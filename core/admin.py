from django.contrib import admin
from .models import questao, teta_usuario
# Register your models here.


class QuestaoAdmin(admin.ModelAdmin):
    ...


class TetaUsuarioAdmin(admin.ModelAdmin):
    ...


admin.site.register(questao, QuestaoAdmin)
admin.site.register(teta_usuario, TetaUsuarioAdmin)
