# Generated by Django 5.1.6 on 2025-02-19 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_location_schedule_alter_user_role_court_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='surface_type',
            field=models.CharField(choices=[('Dirt', 'Dirt'), ('Grass', 'Grass'), ('Clay', 'Clay'), ('Concrete', 'Concrete')], default='Concrete', max_length=25),
        ),
    ]
