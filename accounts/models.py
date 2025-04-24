from django.db import models
from customers.models import Customer
from collects.models import Collect


class Account(models.Model):
    customer_id=models.ForeignKey (
        Customer,
        on_delete=models.PROTECT,
        related_name='accounts',
        verbose_name='Cliente ID',
    )
    balance=models.IntegerField(
        verbose_name='Saldo',
        default=0,
    )


    class Meta:
        verbose_name='Conta'
        verbose_name_plural='Contas'

    def __str__(self):
        return str(self.id)


class Deposit(models.Model):
    colect_id=models.ForeignKey(
        Collect,
        on_delete=models.PROTECT,
        related_name='Deposit',
        verbose_name='Coleta ID',
    )
    account_id=models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name='Deposit',
        verbose_name='Conta ID',
    )
    total=models.IntegerField(
        verbose_name='Total do depósito',
    )
    created_at=models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em',
    )


    class Meta:
        verbose_name='Depósito'
        verbose_name_plural='Depósitos'
    
    def __str__(self):
        return str(self.id)
