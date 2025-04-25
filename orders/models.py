from django.db import models
from customers.models import Customer
from accounts.models import Account
from products.models import Product


class Order (models.Model):
    customer_id=models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name='orders',
        verbose_name='Cliente ID',
    )
    account_id=models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name='orders',
        verbose_name='Conta ID',
    )
    total=models.IntegerField(
        verbose_name='Valor total',
    )
    

    class Meta:
        verbose_name='Pedido'
        verbose_name_plural='Pedidos'
    
    def __str__(self):
        return self.id


class OrderProducts (models.Model):
    order_id=models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
        related_name='orderProducts',
        verbose_name='Pedido ID',
    )
    product_id=models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='orderProducts',
        verbose_name='Pedido ID',
    )
    product_quantity=models.IntegerField(
        verbose_name='Quantidade de produto',
    )
    product_price=models.IntegerField(
        verbose_name='Valor do produto',
    )

    
    class Meta:
        verbose_name='Pedido Produto'
        verbose_name_plural='Pedido produtos'
    
    def __str__(self):
        return self.id