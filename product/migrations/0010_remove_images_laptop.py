# Generated by Django 3.2 on 2021-05-14 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20210514_0207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='laptop',
        ),
    ]
