# Generated by Django 4.2.1 on 2024-10-30 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "equipment",
            "0003_remove_equipment_health_facility_equipmentlocation_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipment",
            name="location",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="equipment",
                to="equipment.equipmentlocation",
            ),
        ),
    ]
