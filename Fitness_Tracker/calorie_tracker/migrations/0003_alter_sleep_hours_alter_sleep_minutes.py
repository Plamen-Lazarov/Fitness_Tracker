# Generated by Django 5.1.3 on 2024-12-11 19:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorie_tracker', '0002_alter_sleep_hours_alter_sleep_minutes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sleep',
            name='hours',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(23)]),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='minutes',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(59)]),
        ),
    ]
