# Generated by Django 5.0.6 on 2024-07-04 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_producto_carrito_carritoitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='carritoitem',
            name='confirmado',
            field=models.BooleanField(default=False),
        ),
    ]