# Generated by Django 3.0 on 2019-12-05 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20191205_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Цена'),
        ),
    ]