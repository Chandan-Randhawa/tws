# Generated by Django 4.0.4 on 2023-04-13 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_products_retreivals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='last_fetched',
            field=models.DateField(null=True),
        ),
    ]
