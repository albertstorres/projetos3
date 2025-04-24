from rest_framework import viewsets
from orders.models import Order, OrderProducts
from orders.serializers import OrderSerializer, OrderProductsSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer


class OrderProductsViewSet(viewsets.ModelViewSet):
    queryset=OrderProducts.objects.all()
    serializer_class=OrderProductsSerializer