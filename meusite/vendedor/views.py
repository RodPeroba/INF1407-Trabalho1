from django.shortcuts import render
from django.views import View
from produtos.models import Produto
from django.contrib.auth.mixins import LoginRequiredMixin

class MeusProdutos(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        contexto = {
            'produtos': Produto.objects.filter(vendedor=request.user.id)
        }
        return render(request, 'vendedor/meusProdutos.html', contexto)