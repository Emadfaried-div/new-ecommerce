# Generated by Django 3.2 on 2021-04-25 18:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0004_auto_20210409_1635'),
        ('orderapp', '0003_alter_order_country'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OderProduct',
            new_name='OrderProduct',
        ),
    ]
