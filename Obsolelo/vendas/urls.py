from django.urls import path
from django.contrib import admin
from vendas import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

app_name = 'vendas'

urlpatterns = [
    # Product URLs
    path('', views.HomePage.as_view(), name='homepage'),
    path('cadastro/', views.CadastroProduto.as_view(), name='cadastro_produto'),
    path("atualizar/<int:pk>/", views.AtualizaProduto.as_view(), name="atualizar_produto"),
    path("comprar/<int:pk>/", views.CompraProduto.as_view(), name="comprar_produto"),
    # User Registration URL
    path('registrar/', views.RegistraUsuario.as_view(), name='registrar_usuario'),
    path("accounts/profile/", LoginView.as_view(template_name='Vendas/login.html'), name='segundo_login'),
    # Login and Logout URLs
    path('login/', LoginView.as_view(template_name='Vendas/login.html',next_page = reverse_lazy('vendas:homepage')), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('vendas:homepage')), name='logout'),
    path("confirmaLogout/", views.ConfirmaLogout.as_view(), name="confirma_logout"),
]