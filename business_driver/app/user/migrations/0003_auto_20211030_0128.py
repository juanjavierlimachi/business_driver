# Generated by Django 3.0.1 on 2021-10-30 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_clienteperfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.PositiveIntegerField(verbose_name='Celular (WhatsApp)'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='Correo Electrónico'),
        ),
    ]
