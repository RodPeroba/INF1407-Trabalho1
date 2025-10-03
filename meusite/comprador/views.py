from django.shortcuts import render
from django.views import View
from produtos.models import Produto
# from comprador.models import CopraProduto
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

class ProdutoIndividual(View):

    def get(self, request, pk, *args, **kwargs):
        produto = Produto.objects.get(id=pk)
        contexto = {'produto': produto}
        return render(request, 'comprador/produtoIndividual.html', contexto)

    def post(self, request, pk, *args, **kwargs):
        produto = Produto.objects.get(id=pk)
        # compra = CopraProduto(
        #     id_produto=produto,
        #     nome_produto=produto.nome,
        #     preco_produto=produto.preco,
        #     id_comprador=request.user,
        #     id_vendedor=produto.vendedor
        # )
        # compra.save()
        produto.delete()
        return HttpResponseRedirect(reverse_lazy('homepage'))
