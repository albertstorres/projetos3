from rest_framework import serializers
from orders.models import Order, OrderProducts


class OrderSerializer(serializers.ModelSerializer):


    class Meta:
        model=Order
        fields='__all__'


class OrderProductsSerializer(serializers.ModelSerializer):


    class Meta:
        model=OrderProducts
        fields='__all__'