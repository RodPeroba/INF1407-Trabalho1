from django.urls import path
from vendas import views

app_name = 'vendas'

urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
    path('cadastro/', views.CadastroProduto.as_view(), name='cadastro_produto'),
    path("atualizar/<int:pk>/", views.AtualizaProduto.as_view(), name="atualizar_produto"),
    path("comprar/<int:pk>/", views.CompraProduto.as_view(), name="comprar_produto"),
]