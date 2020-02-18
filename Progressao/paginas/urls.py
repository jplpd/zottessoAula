from django.urls import path
#Importa as view que a gente criou 
from .views import PaginaInicial, PaginaSobre, PaginaAjuda

# Tem que ser urlpatterns porque é padrão Django
urlpatterns = [
    # Todo path tem endereço, view e nome
    #path('endereco', view, nome da url)
    path('', PaginaInicial.as_view(), name='index'),
    path('sobre', PaginaSobre.as_view(), name='sobre'),
    path('ajuda', PaginaAjuda.as_view(), name='ajuda'),
]
