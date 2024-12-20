# Generated by Django 4.2.1 on 2024-10-16 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnscheduledWorkOrder',
            fields=[
                ('work_order_num', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('problem', models.TextField()),
                ('work_carried', models.CharField(max_length=200)),
                ('work_order_report', models.FileField(blank=True, null=True, upload_to='')),
                ('purchase_order', models.IntegerField(blank=True, null=True)),
                ('update', models.TextField()),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open', max_length=10)),
                ('closed_at', models.DateTimeField(blank=True, null=True)),
                ('date_of_update', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unscheduled_work_orders', to='equipment.equipment')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduledWorkOrder',
            fields=[
                ('work_order_num', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('scheduled_action', models.CharField(choices=[('preventive_maintenance', 'preventive_maintenance'), ('validation', 'validation'), ('inspection', 'inspection')], default='Preventive Maintenance', max_length=200)),
                ('purchase_order', models.IntegerField(blank=True, null=True)),
                ('freq_interval', models.CharField(choices=[('daily', 'daily'), ('weekly', 'weekly'), ('monthly', 'monthly'), ('yearly', 'yearly')], default='Yearly', max_length=225)),
                ('frequency', models.IntegerField()),
                ('next_scheduled_action_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('last_serviced_at', models.DateTimeField()),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scheduled_events', to='equipment.equipment')),
            ],
        ),
    ]
