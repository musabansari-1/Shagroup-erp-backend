# Generated by Django 3.1.2 on 2020-11-26 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_projects', '0005_auto_20201027_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentproject',
            name='degree_backlog',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='studentproject',
            name='puc_backlog',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='studentproject',
            name='sslc_backlog',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]