# Generated by Django 3.1.2 on 2020-11-27 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0016_auto_20201127_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='name',
            field=models.CharField(default='hello python', max_length=40),
            preserve_default=False,
        ),
    ]
