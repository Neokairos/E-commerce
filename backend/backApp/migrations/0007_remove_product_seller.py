# Generated by Django 5.0 on 2023-12-23 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backApp', '0006_alter_product_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Seller',
        ),
    ]