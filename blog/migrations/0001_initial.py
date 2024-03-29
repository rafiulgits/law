# Generated by Django 2.1.7 on 2019-09-19 04:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('Subject', 'Subject'), ('Part', 'Part'), ('Chapter', 'Chapter'), ('Topic', 'Topic'), ('Module', 'Module'), ('Label', 'Label')], max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CQ',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CQTag',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('cq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.CQ')),
            ],
        ),
        migrations.CreateModel(
            name='MCQ',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('option1', models.CharField(max_length=250)),
                ('option2', models.CharField(max_length=250)),
                ('option3', models.CharField(max_length=250)),
                ('option4', models.CharField(max_length=250)),
                ('answer', models.SmallIntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)])),
                ('summary', models.TextField()),
                ('meta', models.CharField(default='', max_length=250)),
                ('entry_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MCQIssue',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('body', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('mcq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.MCQ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MCQLabel',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, unique=True)),
                ('questions', models.ManyToManyField(to='blog.MCQ')),
            ],
        ),
        migrations.CreateModel(
            name='MCQTag',
            fields=[
                ('uid', models.BigAutoField(primary_key=True, serialize=False)),
                ('mcq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.MCQ')),
            ],
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=500)),
                ('body', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('entry_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('name', models.CharField(max_length=250)),
                ('self_loc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='self_loc', serialize=False, to='blog.Path')),
                ('distance', models.SmallIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
                ('root_loc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='root_loc', to='blog.Path')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='folder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Folder'),
        ),
        migrations.AddField(
            model_name='mcqtag',
            name='folder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Folder'),
        ),
        migrations.AddField(
            model_name='cqtag',
            name='folder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Folder'),
        ),
        migrations.AlterUniqueTogether(
            name='mcqtag',
            unique_together={('mcq', 'folder')},
        ),
        migrations.AlterUniqueTogether(
            name='folder',
            unique_together={('self_loc', 'root_loc')},
        ),
        migrations.AlterUniqueTogether(
            name='cqtag',
            unique_together={('cq', 'folder')},
        ),
    ]
