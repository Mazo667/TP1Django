# Generated by Django 5.1 on 2024-08-24 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remitente', models.CharField(max_length=255)),
                ('destinatario', models.CharField(max_length=255)),
            ],
        ),
    ]
