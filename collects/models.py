from django.db import models
from customers.models import Customer


class Address(models.Model):
    customer_id=models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name='Address',
        verbose_name='Cliente ID',
    )
    zip_code=models.CharField(
        max_length=15,
        verbose_name='CEP',
    )
    street_address=models.CharField(
        max_length=50,
        verbose_name='Rua',
    )
    number=models.IntegerField(
        verbose_name='Número',
    )
    complement=models.CharField(
        max_length=60,
        blank=True,
        null=True,
        verbose_name='Complemento',
    )
    neighborhood=models.CharField(
        max_length=50,
        verbose_name='Bairro',
    )


    class Meta:
        verbose_name='Endereço'
        verbose_name_plural='Endereços'
    
    def __str__(self):
        return self.zip_code


class Categorie(models.Model):
    description=models.CharField(
        max_length=50,
        verbose_name='Categoria',
    )
    price=models.IntegerField(
        verbose_name='Preço',
    )


    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
    
    def __str__(self):
        return self.description


class Collect(models.Model):
    categorie_id=models.ForeignKey(
        Categorie,
        on_delete=models.PROTECT,
        related_name='Colect',
        verbose_name='Categoria ID',
    )
    customer_id=models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name='Colect',
        verbose_name='Cliente ID',
    )
    address_id=models.ForeignKey(
        Address,
        on_delete=models.PROTECT,
        related_name='Colect',
        verbose_name='Endereço ID',
    )
    weight=models.IntegerField(
        verbose_name='Peso',
    )
    created_at=models.DateField(
        auto_now_add=True,
        verbose_name='Criado em',
    )


    class Meta:
        verbose_name='Coleta'
        verbose_name_plural='Coletas'
    
    def __str__(self):
        return self.id
