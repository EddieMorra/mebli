# Generated by Django 3.0.2 on 2020-03-26 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20200326_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemprice',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.ItemPrice', verbose_name='Товар'),
        ),
    ]