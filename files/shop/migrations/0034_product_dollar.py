# Generated by Django 3.0.2 on 2020-03-28 03:29

from django.db import migrations
import django.db.models.deletion
import mptt.fields
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0033_auto_20200328_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dollar',
            field=mptt.fields.TreeForeignKey(default=shop.models.dollar, on_delete=django.db.models.deletion.CASCADE, related_name='dollar', to='shop.Dollar', verbose_name='Курс'),
        ),
    ]
