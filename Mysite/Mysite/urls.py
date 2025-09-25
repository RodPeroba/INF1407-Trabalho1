"""
URL configuration for Mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

urlpatterns = [
    # Admin
    path('batata/', admin.site.urls),
    # Apps
    path('comprador/', include('comprador.urls')),
    path('vendedor/', include('vendedor.urls')),
    # Mysite
    # Product URLs
    path('', views.HomePage.as_view(), name='homepage'),
    path('cadastro/', views.CadastroProduto.as_view(), name='cadastro_produto'),
    path("atualizar/<int:pk>/", views.AtualizaProduto.as_view(), name="atualizar_produto"),
    path("comprar/<int:pk>/", views.CompraProduto.as_view(), name="comprar_produto"),
    # User Registration URL
    path('registrar/', views.RegistraUsuario.as_view(), name='registrar_usuario'),
    path("accounts/profile/", LoginView.as_view(template_name='Mysite/login.html'), name='segundo_login'),
    # Login and Logout URLs
    path('login/', LoginView.as_view(template_name='Mysite/login.html',next_page = reverse_lazy('homepage')), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('homepage')), name='logout'),
    path("confirmaLogout/", views.ConfirmaLogout.as_view(), name="confirma_logout"),
]
