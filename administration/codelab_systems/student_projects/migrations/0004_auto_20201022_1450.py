# Generated by Django 3.1.2 on 2020-10-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_projects', '0003_auto_20201022_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentproject',
            name='degree_backlog',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentproject',
            name='puc_backlog',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentproject',
            name='sslc_backlog',
            field=models.BooleanField(default=False),
        ),
    ]
