# Generated by Django 3.2 on 2021-05-15 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20210515_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='new_price',
            new_name='new_pdiscount_pricerice',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='old_price',
            new_name='price',
        ),
    ]