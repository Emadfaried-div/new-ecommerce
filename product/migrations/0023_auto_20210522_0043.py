# Generated by Django 3.2 on 2021-05-21 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_auto_20210522_0042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category_ar',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category_en',
        ),
    ]
