# Generated by Django 3.1.2 on 2020-12-04 13:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_projects', '0013_auto_20201204_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentproject',
            name='degree_backlog',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='studentproject',
            name='puc_backlog',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='studentproject',
            name='sslc_backlog',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]