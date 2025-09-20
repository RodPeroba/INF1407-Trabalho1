from django.shortcuts import render
from django.views import View
from vendas.forms import ProdutoModel2Form
from .models import Produto
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

class HomePage(View):
    def get(self, request, *args, **kwargs):
        vendas_produto = Produto.objects.all()
        contexto = {'vendas_produto': vendas_produto}
        return render(request, 'vendas/homepage.html', contexto)

class CadastroProduto(View):
    def get(self, request, *args, **kwargs):
        contexto = {'form': ProdutoModel2Form()}
        return render(request, 'vendas/cadastroProduto.html', contexto)
    
    def post(self, request, *args, **kwargs):
        form = ProdutoModel2Form(request.POST)
        if form.is_valid():
            form.save()
            contexto = {
                'form': ProdutoModel2Form(),
                'mensagem': 'Produto cadastrado com sucesso!'
            }
            return render(request, 'vendas/cadastroProduto.html', contexto)
        contexto = {'form': form}
        return render(request, 'vendas/cadastroProduto.html', contexto)

class AtualizaProduto(View):
    def get(self, request, pk, *args, **kwargs):
        produto = Produto.objects.get(id=pk)
        form = ProdutoModel2Form(instance=produto)
        contexto = {'form': form}
        return render(request, 'vendas/atualizaProduto.html', contexto)
    
    def post(self, request, pk, *args, **kwargs):
        produto = get_object_or_404(Produto, id=pk)
        form = ProdutoModel2Form(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('vendas:homepage'))
        contexto = {'form': form}
        return render(request, 'vendas/atualizaProduto.html', contexto)

class CompraProduto(View):

    def get(self, request, pk, *args, **kwargs):
        produto = Produto.objects.get(id=pk)
        contexto = {'produto': produto}
        return render(request, 'vendas/comprarProduto.html', contexto)

    def post(self, request, pk, *args, **kwargs):
        produto = Produto.objects.get(id=pk)
        produto.delete()
        return HttpResponseRedirect(reverse_lazy('vendas:homepage'))