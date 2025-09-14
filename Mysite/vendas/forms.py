from django import forms
from vendas.models import Produto

class ProdutoModel2Form(forms.ModelForm):
    class Meta:
        model = Produto
        fields = "__all__"