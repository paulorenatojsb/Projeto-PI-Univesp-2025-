from rest_framework import serializers
from .models import Pedido, ItemPedido

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ['item', 'quantidade']

class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True, write_only=True)
    pedido_id = serializers.UUIDField(read_only=True)  # Inclui o pedido_id na resposta

    class Meta:
        model = Pedido
        fields = ['pedido_id', 'retirada', 'nome_cliente', 'mesa', 'observacoes', 'itens']

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        pedido = Pedido.objects.create(**validated_data)
        for item_data in itens_data:
            ItemPedido.objects.create(pedido=pedido, **item_data)
        return pedido