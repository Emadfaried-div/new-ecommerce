# Generated by Django 3.2 on 2021-05-17 21:34

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0007_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='BroadCast_Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('message', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'BroadCast Email to all Member',
                'verbose_name_plural': 'BroadCast Email',
            },
        ),
    ]
