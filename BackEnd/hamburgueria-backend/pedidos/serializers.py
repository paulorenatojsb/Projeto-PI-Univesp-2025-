from rest_framework import serializers
from .models import Pedido, ItemPedido

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ['item', 'quantidade']

class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['retirada', 'nome_cliente', 'mesa', 'observacoes', 'itens']

    def validate(self, data):
        if not data.get('retirada') and not data.get('mesa'):
            raise serializers.ValidationError("É necessário informar a mesa ou marcar como retirada.")
        if data.get('retirada') and not data.get('nome_cliente'):
            raise serializers.ValidationError("O nome do cliente é obrigatório para retirada.")
        if not data.get('itens') or len(data.get('itens')) == 0:
            raise serializers.ValidationError("O pedido deve conter pelo menos um item.")
        return data

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        pedido = Pedido.objects.create(**validated_data)
        for item_data in itens_data:
            ItemPedido.objects.create(pedido=pedido, **item_data)
        return pedido