# Generated by Django 3.0.2 on 2020-03-28 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_remove_kurs_d_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='kurs_d',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='kurs_d', to='shop.Kurs_d', verbose_name='Курс'),
        ),
    ]
