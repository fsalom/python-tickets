# Generated by Django 5.1.1 on 2024-09-27 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailDBO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('date_raw', models.CharField(max_length=25)),
                ('subject', models.CharField(default='', max_length=150)),
                ('content', models.TextField()),
            ],
        ),
    ]
