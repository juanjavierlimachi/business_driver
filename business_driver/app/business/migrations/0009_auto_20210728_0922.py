# Generated by Django 3.0.1 on 2021-07-28 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_cliente'),
        ('business', '0008_negocio_celular'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='catalogo',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='celular',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='nombre',
        ),
        migrations.AddField(
            model_name='pedido',
            name='precio_unitario',
            field=models.FloatField(default='5'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='total',
            field=models.FloatField(default='5'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_mod', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Cliente')),
                ('negocio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Negocio')),
            ],
            options={
                'verbose_name': 'Orden',
                'verbose_name_plural': 'Ordens',
            },
        ),
    ]