# Generated by Django 3.1.2 on 2020-12-04 13:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0023_auto_20201204_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinternship',
            name='backlog',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]