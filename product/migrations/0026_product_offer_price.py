# Generated by Django 3.2 on 2021-05-30 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_auto_20210528_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offer_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]