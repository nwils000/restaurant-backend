# Generated by Django 5.0.6 on 2024-05-22 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1_restaurant', '0004_rename_contact_info_customer_contact_information_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ManyToManyField(through='app1_restaurant.CustomerOrderLink', to='app1_restaurant.customer'),
        ),
    ]