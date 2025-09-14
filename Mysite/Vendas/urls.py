from django.urls import path
from Vendas import views

app_name = 'Vendas'

urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
]