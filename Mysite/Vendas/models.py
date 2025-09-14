from django.db import models

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100,help_text="Nome do produto")
    vendedor = models.CharField(max_length=100,help_text="Nome do vendedor")
    categoria = models.CharField(max_length=100,help_text="Categoria do produto")
    preco = models.DecimalField(max_digits=8, decimal_places=2,help_text="Preço do produto")
    foto = models.ImageField(upload_to='fotos_produtos/', null=True, blank=True, help_text="Foto do produto")
    descricao = models.TextField(help_text="Descrição do produto")

    def __str__(self):
        return self.nome