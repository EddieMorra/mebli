# Generated by Django 3.0.2 on 2020-03-28 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0035_remove_product_dollar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dollar',
            name='num',
            field=models.FloatField(verbose_name='Курс валют'),
        ),
    ]