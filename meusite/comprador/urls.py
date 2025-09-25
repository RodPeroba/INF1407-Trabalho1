from django.urls import path
from comprador import views

app_name = 'comprador'

urlpatterns = [

    path("<str:categoria>/<str:nome>/<int:pk>/", views.ProdutoIndividual.as_view(), name="produto_individual")
    
]