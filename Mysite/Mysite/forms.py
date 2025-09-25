from django import forms
from produtos.models import Produto

class ProdutoModel2Form(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'preco', 'foto', 'descricao']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})