# Generated by Django 3.1.6 on 2021

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('email', models.EmailField(max_length=50)),
                ('location', models.CharField(max_length=50, verbose_name='Localização')),
                ('role', models.PositiveSmallIntegerField(choices=[(2, 'Cliente'), (3, 'Vendedor(a)')], null=True, verbose_name='Atribuição')),
                ('creationDate', models.DateTimeField(verbose_name='Data de Entrada')),
                ('attDate', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Vendedor(a)',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('email', models.EmailField(max_length=50)),
                ('location', models.CharField(max_length=50, verbose_name='Localização')),
                ('role', models.PositiveSmallIntegerField(choices=[(2, 'Cliente'), (3, 'Vendedor(a)')], null=True, verbose_name='Atribuição')),
                ('creationDate', models.DateTimeField(verbose_name='Data de Entrada')),
                ('attDate', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Cliente',
            },
        ),
    ]
