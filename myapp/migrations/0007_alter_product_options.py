# Generated by Django 4.0.4 on 2023-04-12 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_product_last_fetched'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'managed': False},
        ),
    ]
