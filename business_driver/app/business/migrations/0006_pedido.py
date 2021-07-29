# Generated by Django 3.0.1 on 2021-07-10 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0005_auto_20210706_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Tu Nombre Completo')),
                ('celular', models.PositiveIntegerField(verbose_name='Tu Número de Celular')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_mod', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
                ('catalogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Catalogo')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]