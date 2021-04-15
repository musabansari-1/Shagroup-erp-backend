# Generated by Django 3.1.2 on 2020-12-04 11:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0022_auto_20201204_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinternship',
            name='backlog',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='academicinternship',
            name='overall_percentage',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]