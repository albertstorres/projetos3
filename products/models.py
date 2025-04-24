from django.db import models


class Product(models.Model):
    name=models.CharField(
        max_length=100,
        unique=True,
    )
    price=models.IntegerField(
        verbose_name='Preço',
    )


    class Meta:
        verbose_name='Produto'
        verbose_name_plural='Produtos'

    def __str__ (self):
        return self.name
