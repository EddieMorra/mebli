# Generated by Django 3.0.2 on 2020-03-05 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20200305_1619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='price_usd',
            new_name='price',
        ),
    ]