# Generated by Django 5.0.6 on 2024-05-23 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1_restaurant', '0011_order_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='customer_order_details',
        ),
    ]