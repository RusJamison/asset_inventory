# Generated by Django 4.2.1 on 2024-10-23 12:19

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work_orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unscheduledworkorder',
            name='work_order_report',
            field=cloudinary.models.CloudinaryField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
