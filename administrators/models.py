from django.db import models
from django.contrib.auth.models import User


class Administrator(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.PROTECT,
        blank = True,
        null = True,
        related_name = 'administrators',
        verbose_name = 'Administrador',
    )
    first_name = models.CharField(
        max_length = 50,
        verbose_name = 'Primeiro nome',
    )
    last_name = models.CharField(
        max_length = 50,
        verbose_name = 'Sobrenome',
    )
    email = models.EmailField(
        max_length = 100,
        unique = True,
        db_index = True,
        verbose_name = 'E-mail', 
    )
    

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'

    def __str__(self):
        return self.first_name