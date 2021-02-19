# Generated by Django 2.1.7 on 2019-09-19 04:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MCQExam',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('is_clone', models.BooleanField(default=False)),
                ('is_public', models.BooleanField(default=False)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MCQExamItem',
            fields=[
                ('uid', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MCQExamSource',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('public', models.BooleanField(default=False)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('total_mcq', models.PositiveSmallIntegerField()),
                ('duration', models.PositiveSmallIntegerField()),
                ('statistics', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MCQReport',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('total_correct', models.PositiveSmallIntegerField()),
                ('total_wrong', models.PositiveSmallIntegerField()),
                ('total_blank', models.PositiveSmallIntegerField()),
                ('result', models.FloatField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('exam', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exam.MCQExam')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OMR',
            fields=[
                ('uid', models.BigAutoField(primary_key=True, serialize=False)),
                ('answer', models.SmallIntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)])),
                ('correct', models.BooleanField()),
                ('mcq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.MCQ')),
                ('report', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam.MCQReport')),
            ],
        ),
        migrations.AddField(
            model_name='mcqexamitem',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.MCQExamSource'),
        ),
        migrations.AddField(
            model_name='mcqexamitem',
            name='mcq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.MCQ'),
        ),
        migrations.AddField(
            model_name='mcqexam',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.MCQExamSource'),
        ),
        migrations.AlterUniqueTogether(
            name='mcqexamitem',
            unique_together={('mcq', 'exam')},
        ),
    ]