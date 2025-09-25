from django.urls import path
from vendedor import views

app_name = 'vendedor'

urlpatterns = [
    path('meusprodutos/', views.MeusProdutos.as_view(), name='meus_produtos'),
    
]