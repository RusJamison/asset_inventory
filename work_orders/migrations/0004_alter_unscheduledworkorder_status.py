# Generated by Django 4.2.1 on 2024-10-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_orders', '0003_remove_scheduledworkorder_frequency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unscheduledworkorder',
            name='status',
            field=models.CharField(blank=True, choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open', max_length=100),
        ),
    ]
