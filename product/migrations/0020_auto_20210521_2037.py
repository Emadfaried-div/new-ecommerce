# Generated by Django 3.2 on 2021-05-21 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_product_detail_ar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at_ar',
        ),
        migrations.RemoveField(
            model_name='product',
            name='detail_ar',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name_ar',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title_ar',
        ),
    ]
