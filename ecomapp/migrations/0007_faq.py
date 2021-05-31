# Generated by Django 3.2 on 2021-05-04 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0006_delete_shopcart'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordernumber', models.IntegerField()),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField()),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], default=False, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]