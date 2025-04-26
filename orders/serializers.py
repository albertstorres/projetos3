from rest_framework import serializers
from orders.models import Order, OrderProducts
from django.db import transaction
from products.models import Product


class OrderProductInputSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    product_quantity = serializers.IntegerField(min_value=1)
    product_price = serializers.IntegerField(min_value=0)

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Produto não encontrado.")
        return value


class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductInputSerializer(many=True, write_only=True)


    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['total']

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        customer = validated_data['customer_id']
        account = validated_data['account_id']
        total = 0

        for item in products_data:
            subtotal = item['product_price'] * item['product_quantity']
            total += subtotal

        if account.customer_id != customer:
            raise serializers.ValidationError('A conta não pertence ao cliente')

        if account.balance < total:
            raise serializers.ValidationError('Saldo insuficiente.')

        with transaction.atomic():
            account.balance -= total
            account.save()

            order = Order.objects.create(total=total, **validated_data)

            for item in products_data:
                OrderProducts.objects.create(
                    order_id=order,
                    product_id_id=item['product_id'],
                    product_quantity=item['product_quantity'],
                    product_price=item['product_price']
                )

        return order


class OrderProductsSerializer(serializers.ModelSerializer):


    class Meta:
        model = OrderProducts
        fields = '__all__'