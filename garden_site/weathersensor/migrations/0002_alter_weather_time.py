# Generated by Django 5.0.4 on 2024-05-14 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weathersensor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
