# Generated by Django 3.0.1 on 2021-07-28 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0009_auto_20210728_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='orden',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='business.Orden'),
            preserve_default=False,
        ),
    ]
