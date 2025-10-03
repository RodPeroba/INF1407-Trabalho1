from django.shortcuts import render
from django.views import View
from .forms import ProdutoModel2Form
from produtos.models import Categoria, Produto
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView


class HomePage(View):
    
    def get(self, request, *args, **kwargs):
        user_groups = request.user.groups.all() if request.user.is_authenticated else []
        vendas_produto = Produto.objects.all()
        categorias_choices = Categoria.choices
        categorias = []
        for categoria in categorias_choices:
            categorias.append(categoria[1])
        contexto = {'vendas_produto': vendas_produto, 'user_groups': user_groups, 'categorias': categorias}
        return render(request, 'main/homepage.html', contexto)


class CadastroProduto(View):
    
    def get(self, request, *args, **kwargs):
        contexto = {'form': ProdutoModel2Form()}
        return render(request, 'main/cadastroProduto.html', contexto)
    
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
            return render(request, 'main/cadastroProduto.html', contexto)
        contexto = {'form': form}
        return render(request, 'main/cadastroProduto.html', contexto)

class AtualizaProduto(View):
    
    def get(self, request, pk, *args, **kwargs):
        produto = Produto.objects.get(id=pk)
        form = ProdutoModel2Form(instance=produto)
        contexto = {'form': form}
        return render(request, 'main/atualizaProduto.html', contexto)
    
    def post(self, request, pk, *args, **kwargs):
        produto = get_object_or_404(Produto, id=pk)
        form = ProdutoModel2Form(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('homepage'))
        contexto = {'form': form}
        return render(request, 'main/atualizaProduto.html', contexto)

class RegistraUsuario(View):
    
    def get(self, request, *args, **kwargs):
        formulario = UserCreationForm()
        contexto = {'formulario': formulario}
        return render(request, 'main/registrarUsuario.html', contexto)

    def post(self, request, *args, **kwargs):
        formulario = UserCreationForm(request.POST)
        tipo_usuario = request.POST.get('tipo_usuario')
        if formulario.is_valid():
            user = formulario.save()
            # Adicionar ao grupo baseado no tipo
            if tipo_usuario == 'vendedor':
                grupo_vendedor, created = Group.objects.get_or_create(name='Vendedor')
                user.groups.add(grupo_vendedor)
            elif tipo_usuario == 'comprador':
                grupo_comprador, created = Group.objects.get_or_create(name='Comprador')
                user.groups.add(grupo_comprador)

            return HttpResponseRedirect(reverse_lazy('homepage'))
        contexto = {'formulario': formulario}
        return render(request, 'main/registrarUsuario.html', contexto)
    
class ConfirmaLogout(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'main/logout.html')
    
class PaginaCategoria(View):

    def get(self, request, categoria, *args, **kwargs):
        '''
        Exibe a página de produtos por categoria.
        Parâmetros:
        - categoria: String com o rótulo da categoria selecionada.
        '''
        categorias_choices = Categoria.choices
        categoria_atual_label = None
        for cat in categorias_choices:
            if cat[1] == categoria:
                categoria_atual_label = cat[0]
                break
        produtos = Produto.objects.filter(categoria=categoria_atual_label)

        contexto = {'produtos': produtos, 'categorias': categorias_choices, 'categoria_atual_rotulo': categoria}
        return render(request, 'main/paginaCategoria.html', contexto)
    
class MeuUpdateView(UpdateView):
    def get(self, request, pk, *args, **kwargs):
        if request.user.id == pk:
            return super().get(request, pk, *args, **kwargs)
        else:
            return redirect('homepage')
    def post(self, request, pk, *args, **kwargs):
        return redirect('homepage')