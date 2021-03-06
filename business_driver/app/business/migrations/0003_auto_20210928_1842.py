# Generated by Django 3.0.1 on 2021-09-28 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20210801_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='negocio',
            name='plan_basic',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='negocio',
            name='plan_premiun',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='negocio',
            name='celular',
            field=models.PositiveIntegerField(verbose_name='Num. de Celular (WhatsApp)'),
        ),
        migrations.AlterField(
            model_name='negocio',
            name='imagen',
            field=models.ImageField(blank=True, help_text='Opcional', null=True, upload_to='img_negocios', verbose_name='Imagen de portada'),
        ),
    ]
