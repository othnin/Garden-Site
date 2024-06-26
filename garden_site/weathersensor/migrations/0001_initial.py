# Generated by Django 5.0.4 on 2024-05-14 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('lon', models.FloatField(default=0.0)),
                ('lat', models.FloatField(default=0.0)),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('temp', models.DecimalField(decimal_places=2, max_digits=5)),
                ('feels_like', models.DecimalField(decimal_places=2, max_digits=5)),
                ('temp_min', models.DecimalField(decimal_places=2, max_digits=5)),
                ('temp_max', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pressure', models.FloatField()),
                ('humidity', models.FloatField()),
                ('visibility', models.FloatField()),
                ('wind_speed', models.FloatField()),
                ('wind_deg', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sunrise', models.DateTimeField()),
                ('sunset', models.DateTimeField()),
                ('time', models.DateTimeField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weathersensor.city')),
            ],
        ),
    ]
