from django.db import models


class Customer(models.Model):
    username=models.CharField(
        max_length=50,
        unique=True,
        default='client',
        verbose_name='Login',
    )
    first_name=models.CharField(
        max_length=50, 
        verbose_name='Primeiro nome'
        )
    last_name=models.CharField(
        max_length=50, 
        verbose_name='Sobrenome'
        )
    email=models.EmailField(
        max_length=100,
        unique=True,
        db_index=True,
        verbose_name='E-mail',
    )
    is_staff=models.BooleanField(
        default=False,
        verbose_name='Privilégio',
    )


    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
    
    def __str__(self):
        return self.first_name
    
