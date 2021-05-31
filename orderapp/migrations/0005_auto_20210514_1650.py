# Generated by Django 3.2 on 2021-05-14 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_imagess'),
        ('orderapp', '0004_rename_oderproduct_orderproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='laptop',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.laptop'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopcart',
            name='laptop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.laptop'),
        ),
    ]