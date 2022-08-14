from django.contrib import admin
from django.urls import path

from base.views import home, cadastro, pag_inicial, consultar_quest, logout_view, nav_quest
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cadastro', cadastro, name='cadastro'),
    path('pagina-inicial', pag_inicial, name='pagina-inicial'),
    path('consultar-questoes', consultar_quest, name='consultar'),
    path('logout', logout_view, name="logout"),
    #path('nav-quest', nav_quest, name="nav-quest"),
    path('<str:assunto>/<str:disciplina>', nav_quest),

]
