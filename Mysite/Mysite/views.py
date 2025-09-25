from django.shortcuts import render
from django.views import View
from .forms import ProdutoModel2Form
from produtos.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate, logout


class HomePage(View):
    
    def get(self, request, *args, **kwargs):
        user_groups = request.user.groups.all() if request.user.is_authenticated else []
        vendas_produto = Produto.objects.all()
        categorias_choices = Categoria.choices
        categorias = []
        for categoria in categorias_choices:
            categorias.append(categoria[1])
        contexto = {'vendas_produto': vendas_produto, 'user_groups': user_groups, 'categorias': categorias}
        return render(request, 'Mysite/homepage.html', contexto)


class CadastroProduto(View):
    
    def get(self, request, *args, **kwargs):
        contexto = {'form': ProdutoModel2Form()}
        return render(request, 'Mysite/cadastroProduto.html', contexto)
    
    def post(self, request, *args, **kwargs):
        form = ProdutoModel2Form(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.vendedor = request.user
            produto.save()
            contexto = {
                'form': ProdutoModel2Form(),
                'mensagem': 'Produto cadastrado com sucesso!'
            }
            return render(request, 'Mysite/cadastroProduto.html', contexto)
        contexto = {'form': form}
        return render(request, 'Mysite/cadastroProduto.html', contexto)

class AtualizaProduto(View):
    
    def get(self, request, pk, *args, **kwargs):
        produto = Produto.objects.get(id=pk)
        form = ProdutoModel2Form(instance=produto)
        contexto = {'form': form}
        return render(request, 'Mysite/atualizaProduto.html', contexto)
    
    def post(self, request, pk, *args, **kwargs):
        produto = get_object_or_404(Produto, id=pk)
        form = ProdutoModel2Form(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('homepage'))
        contexto = {'form': form}
        return render(request, 'Mysite/atualizaProduto.html', contexto)

class CompraProduto(View):

    def get(self, request, pk, *args, **kwargs):
        produto = Produto.objects.get(id=pk)
        contexto = {'produto': produto}
        return render(request, 'Mysite/comprarProduto.html', contexto)

    def post(self, request, pk, *args, **kwargs):
        produto = Produto.objects.get(id=pk)
        produto.delete()
        return HttpResponseRedirect(reverse_lazy('homepage'))
    
class RegistraUsuario(View):
    
    def get(self, request, *args, **kwargs):
        formulario = UserCreationForm()
        contexto = {'formulario': formulario}
        return render(request, 'Mysite/registrarUsuario.html', contexto)

    def post(self, request, *args, **kwargs):
        formulario = UserCreationForm(request.POST)
        tipo_usuario = request.POST.get('tipo_usuario')
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse_lazy('homepage'))
        formulario = UserCreationForm()
        contexto = {'formulario': formulario}
        return render(request, 'Mysite/registrarUsuario.html', contexto)
    
class ConfirmaLogout(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'Mysite/logout.html')