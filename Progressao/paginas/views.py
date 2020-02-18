from django.shortcuts import render

#Importar o TemplateView para criar páginas simples
from django.views.generic import TemplateView


# Create your views here.

# A clasee PaginaInicial "extends" TemplateView
class PaginaInicial(TemplateView):
    #Toda classe filha do TemplateView prescisa do ateributo abaixo para definir um template a ser rederizado

    template_name = 'paginas/index.html'

class PaginaSobre(TemplateView):

    template_name = 'paginas/sobre.html'


class PaginaAjuda(TemplateView):

    template_name = 'paginas/ajuda.html'
