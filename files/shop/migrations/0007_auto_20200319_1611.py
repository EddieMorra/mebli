# Generated by Django 3.0.2 on 2020-03-19 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200319_1547'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created'], 'verbose_name': 'Відгук', 'verbose_name_plural': 'Відгуки'},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Текст'),
        ),
    ]
