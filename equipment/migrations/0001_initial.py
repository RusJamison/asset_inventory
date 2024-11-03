# Generated by Django 4.2.1 on 2024-10-16 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="HealthFacility",
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
                ("name", models.CharField(max_length=225)),
                ("location", models.CharField(max_length=225)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name_plural": "Health Facilities",
            },
        ),
        migrations.CreateModel(
            name="Manufacturer",
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
                ("name", models.CharField(default="Company", max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name_plural": "Manufacturers",
            },
        ),
        migrations.CreateModel(
            name="ServiceProvider",
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
                ("name", models.CharField(max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name_plural": "Service Providers",
            },
        ),
        migrations.CreateModel(
            name="Equipment",
            fields=[
                ("name", models.CharField(max_length=200)),
                ("model", models.CharField(max_length=250)),
                (
                    "asset_tag",
                    models.IntegerField(
                        default=0, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("serial_no", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="equipment_images/"
                    ),
                ),
                ("notes", models.TextField(null=True)),
                ("user_manual", models.FileField(upload_to="equipment_images/")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("in use", "in use"),
                            ("under repair", "under repair"),
                            ("available", "available"),
                            ("decommissioned", "decommissioned"),
                        ],
                        default="in use",
                        max_length=250,
                    ),
                ),
                ("purchase_order_number", models.CharField(blank=True, max_length=50)),
                ("warranty_start_date", models.DateField()),
                ("warranty_end_date", models.DateField()),
                ("in_use_as_of_date", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="equipments",
                        to="equipment.category",
                    ),
                ),
                (
                    "health_facility",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="equipments",
                        to="equipment.healthfacility",
                    ),
                ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="equipments",
                        to="equipment.manufacturer",
                    ),
                ),
                (
                    "service_provider",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="equipments",
                        to="equipment.serviceprovider",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Equipment",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Department",
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
                ("name", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "health_facility",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="departments",
                        to="equipment.healthfacility",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Departments",
            },
        ),
    ]
