# Generated by Django 4.0.5 on 2023-10-28 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_categoria_nombre'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='coleccion_producto',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='coleccion_producto',
            name='coleccion',
        ),
        migrations.RemoveField(
            model_name='coleccion_producto',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='historial',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='producto_pedido',
            name='producto',
        ),
        migrations.AlterField(
            model_name='producto',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.DeleteModel(
            name='Coleccion',
        ),
        migrations.DeleteModel(
            name='Coleccion_Producto',
        ),
        migrations.DeleteModel(
            name='Historial',
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
        migrations.DeleteModel(
            name='Producto_Pedido',
        ),
    ]
