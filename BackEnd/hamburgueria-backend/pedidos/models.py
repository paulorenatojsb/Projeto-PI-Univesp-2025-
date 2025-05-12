from django.db import models
from menu.models import MenuItem

class Pedido(models.Model):
    retirada = models.BooleanField(default=False)
    nome_cliente = models.CharField(max_length=255, blank=True, null=True)
    mesa = models.IntegerField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade}x {self.item.nome}"