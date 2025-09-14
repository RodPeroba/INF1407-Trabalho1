from django.shortcuts import render
from django.views import View


class HomePage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Vendas/homepage.html')