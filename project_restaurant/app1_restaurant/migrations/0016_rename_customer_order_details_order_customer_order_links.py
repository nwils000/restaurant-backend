# Generated by Django 5.0.6 on 2024-05-23 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1_restaurant', '0015_rename_food_item_details_customerorderdetail_food_order_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer_order_details',
            new_name='customer_order_links',
        ),
    ]
