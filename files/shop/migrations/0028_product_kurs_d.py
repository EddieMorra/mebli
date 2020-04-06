# Generated by Django 3.0.2 on 2020-03-28 02:45

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_product_kurs'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='kurs_d',
            field=mptt.fields.TreeForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='kurs_d', to='shop.Kurs_d', verbose_name='Курс'),
        ),
    ]