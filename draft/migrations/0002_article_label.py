# Generated by Django 2.1.7 on 2019-10-28 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='label',
            field=models.CharField(default='', max_length=50),
        ),
    ]