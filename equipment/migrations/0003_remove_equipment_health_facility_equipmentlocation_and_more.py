# Generated by Django 4.2.1 on 2024-10-26 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("equipment", "0002_alter_equipment_image_alter_equipment_user_manual"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="equipment",
            name="health_facility",
        ),
        migrations.CreateModel(
            name="EquipmentLocation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="equipment_location",
                        to="equipment.department",
                    ),
                ),
                (
                    "health_facility",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="equipment_location",
                        to="equipment.healthfacility",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="equipment",
            name="location",
            field=models.ForeignKey(
                default=7000103,
                on_delete=django.db.models.deletion.CASCADE,
                to="equipment.equipmentlocation",
            ),
            preserve_default=False,
        ),
    ]
