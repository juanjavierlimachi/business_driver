# Generated by Django 3.0.1 on 2021-06-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_clienteperfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_servicio', models.CharField(max_length=50, unique=True, verbose_name='Nombre del servicio')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_mod', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Categoria  ',
                'verbose_name_plural': 'Servicio',
            },
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Correo Electrónico'),
        ),
    ]
