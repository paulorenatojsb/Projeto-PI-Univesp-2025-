from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pedido
from .serializers import PedidoSerializer
import logging

logger = logging.getLogger('custom_logger')

class PedidoAPIView(APIView):
    def post(self, request):
        logger.info(f"Payload recebido: {request.data}")  # Log do payload recebido
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                pedido = serializer.save()
                logger.info(f"Pedido criado com sucesso: {pedido.id}")  # Log do pedido criado
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                logger.error(f"Erro ao salvar pedido: {str(e)}")  # Log do erro
                return Response({"error": "Erro ao salvar pedido."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        logger.error(f"Erros de validação: {serializer.errors}")  # Log dos erros de validação
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)