# Generated by Django 3.0.2 on 2020-03-28 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20200328_0440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='kurs_d',
        ),
    ]