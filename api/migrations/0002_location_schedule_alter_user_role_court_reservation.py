# Generated by Django 5.1.6 on 2025-02-19 22:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_hour', models.TimeField()),
                ('end_hour', models.TimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('User', 'User'), ('Trainer', 'Trainer')], default='User', max_length=50),
        ),
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surface_type', models.CharField(choices=[('Dirt', 'Dirt'), ('Grass', 'Grass'), ('Clay', 'Clay'), ('Concrete', 'Concrete')], default='Concrete', max_length=25)),
                ('max_players', models.PositiveIntegerField()),
                ('court_price', models.PositiveIntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.location')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.schedule')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('is_paid', models.BooleanField(default=False)),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.court')),
                ('participants', models.ManyToManyField(limit_choices_to={'role': 'User'}, related_name='participants', to=settings.AUTH_USER_MODEL)),
                ('trainer', models.ForeignKey(limit_choices_to={'role': 'Trainer'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
