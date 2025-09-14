from django.urls import path
from vendas import views

app_name = 'vendas'

urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
    path('cadastro/', views.CadastroProduto.as_view(), name='cadastro_produto'),
]