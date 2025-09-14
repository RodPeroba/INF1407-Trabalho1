from django.shortcuts import render
from django.views import View
from vendas.forms import ProdutoModel2Form

class HomePage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vendas/homepage.html')

class CadastroProduto(View):
    def get(self, request, *args, **kwargs):
        contexto = {'form': ProdutoModel2Form()}
        return render(request, 'vendas/cadastroProduto.html', contexto)