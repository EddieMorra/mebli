# Generated by Django 3.0.2 on 2020-03-26 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_itemprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemprice',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='Товар'),
        ),
    ]
