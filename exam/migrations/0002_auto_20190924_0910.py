# Generated by Django 2.1.7 on 2019-09-24 03:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='omr',
            name='answer',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)]),
        ),
    ]
