# Generated by Django 3.2 on 2021-06-09 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0029_auto_20210608_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]