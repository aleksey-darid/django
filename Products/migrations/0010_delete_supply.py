# Generated by Django 4.0.2 on 2022-03-08 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0009_remove_bid_supplier_bid_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Supply',
        ),
    ]