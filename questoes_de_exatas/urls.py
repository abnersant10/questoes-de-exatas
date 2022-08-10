from django.contrib import admin
from django.urls import path
from base.views import home, cadastro, pag_inicial, consultar, logout_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cadastro', cadastro, name='cadastro'),
    path('pagina-inicial', pag_inicial, name='pagina-inicial'),
    path('consultar-questoes', consultar, name='consultar'),
    path('logout', logout_view, name="logout"),
]
