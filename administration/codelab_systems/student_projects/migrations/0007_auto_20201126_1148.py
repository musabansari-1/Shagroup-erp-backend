# Generated by Django 3.1.2 on 2020-11-26 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_projects', '0006_auto_20201126_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TrainerRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='studentproject',
            name='role',
        ),
    ]