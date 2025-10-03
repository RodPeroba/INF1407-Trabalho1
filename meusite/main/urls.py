"""
URL configuration for main project.

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
from main import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

urlpatterns = [
    # Admin
    path("batata/", admin.site.urls),
    # Apps
    path("comprador/", include("comprador.urls")),
    path("vendedor/", include("vendedor.urls")),
    # main
    # Product URLs
    path("", views.HomePage.as_view(), name="homepage"),
    path("cadastro/", views.CadastroProduto.as_view(), name="cadastro_produto"),
    path(
        "atualizar/<int:pk>/", views.AtualizaProduto.as_view(), name="atualizar_produto"
    ),
    path(
        "produtos/<str:categoria>/",
        views.PaginaCategoria.as_view(),
        name="pagina_categoria",
    ),
    # User Registration URL
    path("registrar/", views.RegistraUsuario.as_view(), name="registrar_usuario"),
    path(
        "accounts/profile/",
        LoginView.as_view(template_name="main/login.html"),
        name="segundo_login",
    ),
    # Login and Logout URLs
    path(
        "login/",
        LoginView.as_view(
            template_name="main/login.html", next_page=reverse_lazy("homepage")
        ),
        name="login",
    ),
    path(
        "logout/", LogoutView.as_view(next_page=reverse_lazy("homepage")), name="logout"
    ),
    path("confirmaLogout/", views.ConfirmaLogout.as_view(), name="confirma_logout"),
    # Troca de Senha
    path(
        "trocaSenha/",
        PasswordChangeView.as_view(
            template_name="contas/password_change_form.html",
            success_url=reverse_lazy("troca_senha_feito"),
        ),
        name="troca_senha",
    ),
    path(
        "trocaSenhaFeito/",
        PasswordChangeDoneView.as_view(
            template_name="contas/password_change_done.html"
        ),
        name="troca_senha_feito",
    ),
    # path(
    #     "contas/editarPerfil/<int:pk>",
    #     UpdateView.as_view(
    #         template_name="contas/user_form.html",
    #         model=User,
    #         fields=["first_name", "last_name", "email"],
    #         success_url=reverse_lazy("homepage"),
    #     ),
    #     name="editar_perfil",
    # ),
    path(
        "contas/editarPerfilSeguro/<int:pk>/",
        views.MeuUpdateView.as_view(
            template_name="contas/user_form.html",
            model=User,
            fields=["first_name", "last_name", "email"],
            success_url=reverse_lazy("homepage"),
        ),
        name="editar_perfil_seguro",
    ),
    # Reset de Senha
    path(
        "contas/trocaSenha/",
        PasswordResetView.as_view(
            template_name="contas/password_reset_form.html",
            email_template_name="contas/password_reset_email.html",
            subject_template_name="contas/password_reset_subject.html",
            success_url=reverse_lazy("password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "contas/trocaSenhaFeito/",
        PasswordResetDoneView.as_view(
            template_name="contas/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "contas/reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="contas/password_reset_confirm.html",
            success_url=reverse_lazy("password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "contas/password_reset_complete/",
        PasswordResetCompleteView.as_view(
            template_name="contas/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
