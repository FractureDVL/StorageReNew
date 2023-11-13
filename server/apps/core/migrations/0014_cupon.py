# Generated by Django 4.0.5 on 2023-10-29 14:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_productopedido_producto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cupon', models.CharField(max_length=255, unique=True, verbose_name='Cupon')),
                ('descuento', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='El descuento no puede ser negativo')], verbose_name='Descuento')),
                ('vencimiento', models.DateField(verbose_name='Vencimiento')),
            ],
            options={
                'verbose_name': 'Cupon',
                'verbose_name_plural': 'Cupones',
            },
        ),
    ]
