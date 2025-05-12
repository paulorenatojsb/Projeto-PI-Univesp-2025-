from django.urls import path
from .views import PedidoAPIView

urlpatterns = [
    path('', PedidoAPIView.as_view(), name='pedido-api'),  # Define o endpoint base
]