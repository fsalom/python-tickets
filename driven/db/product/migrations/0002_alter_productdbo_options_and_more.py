# Generated by Django 5.1.1 on 2024-10-24 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productdbo',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterModelOptions(
            name='productpricehistorydbo',
            options={'verbose_name': 'Relación historia precio producto', 'verbose_name_plural': 'Relación historia precio productos'},
        ),
    ]