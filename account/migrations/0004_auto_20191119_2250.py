# Generated by Django 2.1.7 on 2019-11-19 16:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_reset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reset',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]