# Generated by Django 3.2 on 2021-05-15 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0005_auto_20210514_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='laptop',
        ),
        migrations.RemoveField(
            model_name='shopcart',
            name='laptop',
        ),
    ]