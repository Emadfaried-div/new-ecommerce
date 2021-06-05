# Generated by Django 3.2 on 2021-06-05 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0028_product_seller'),
        ('orderapp', '0006_auto_20210515_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='seller',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='product.seller'),
            preserve_default=False,
        ),
    ]