# Generated by Django 4.2.1 on 2024-10-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_orders', '0002_alter_unscheduledworkorder_work_order_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduledworkorder',
            name='frequency',
        ),
        migrations.AlterField(
            model_name='scheduledworkorder',
            name='last_serviced_at',
            field=models.DateField(),
        ),
    ]
