from django.shortcuts import render
from django.views import View
from produtos.models import Produto
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

class ProdutoIndividual(View):

    def get(self, request, pk, *args, **kwargs):
        produto = Produto.objects.get(id=pk)
        contexto = {'produto': produto}
        return render(request, 'comprador/produtoIndividual.html', contexto)

    def post(self, request, pk, *args, **kwargs):
        produto = Produto.objects.get(id=pk)
        produto.delete()
        return HttpResponseRedirect(reverse_lazy('main:homepage'))
