# from django.db import models
# from produtos.models import Produto
# from django.contrib.auth.models import User

# class CopraProduto(models.Model):
#     id_produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
#     nome_produto = models.CharField(max_length=100)
#     preco_produto = models.DecimalField(max_digits=10, decimal_places=2)
#     id_comprador = models.ForeignKey(User, on_delete=models.PROTECT, related_name='comprador')
#     id_vendedor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='vendedor')
#     data_compra = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return self.nome_produto
