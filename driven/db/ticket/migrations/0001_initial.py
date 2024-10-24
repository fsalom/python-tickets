# Generated by Django 5.1.1 on 2024-09-27 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TicketDBO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('date_raw', models.CharField(max_length=25)),
                ('total', models.FloatField()),
                ('id_ticket', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TicketProductDBO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=0)),
                ('units', models.FloatField(default=1)),
            ],
        ),
    ]
