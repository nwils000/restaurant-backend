# Generated by Django 5.0.6 on 2024-05-22 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1_restaurant', '0005_order_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerorderdetail',
            name='quantity',
        ),
    ]