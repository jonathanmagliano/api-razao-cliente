from django.db import models
from django.contrib.auth.models import User

# Create models


class Client(models.Model):
    ROLE_CHOICES = (
        (2, 'Cliente'),
        (3, 'Vendedor(a)'),
    )
    name = models.CharField(max_length=50, verbose_name='Nome')
    email = models.EmailField(max_length=50)
    location = models.CharField(max_length=50, verbose_name='Localização')
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, verbose_name='Atribuição')
    creationDate = models.DateTimeField(verbose_name='Data de Entrada')
    attDate = models.DateTimeField(auto_now=True, verbose_name='Última atualização')
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Cliente'

    def __str__(self):
        return self.name


class Seller(models.Model):
    ROLE_CHOICES = (
        (2, 'Cliente'),
        (3, 'Vendedor(a)'),
    )
    name = models.CharField(max_length=50, verbose_name='Nome')
    email = models.EmailField(max_length=50)
    location = models.CharField(max_length=50, verbose_name='Localização')
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, verbose_name='Atribuição')
    creationDate = models.DateTimeField(verbose_name='Data de Entrada')
    attDate = models.DateTimeField(auto_now=True, verbose_name='Última atualização')
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Vendedor(a)'

    def __str__(self):
        return self.name
