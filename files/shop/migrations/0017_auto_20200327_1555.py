# Generated by Django 3.0.2 on 2020-03-27 13:55

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20200327_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.Category', verbose_name='Категорія'),
        ),
    ]
