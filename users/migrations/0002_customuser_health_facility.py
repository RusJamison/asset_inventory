# Generated by Django 4.2.1 on 2024-11-09 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("equipment", "0005_alter_equipment_image_alter_equipment_notes_and_more"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="health_facility",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="equipment.healthfacility",
            ),
            preserve_default=False,
        ),
    ]
