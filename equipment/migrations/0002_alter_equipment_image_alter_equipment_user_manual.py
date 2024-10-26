# Generated by Django 4.2.1 on 2024-10-21 18:58

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='image',
            field=cloudinary.models.CloudinaryField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='equipment',
            name='user_manual',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]