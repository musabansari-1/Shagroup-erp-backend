# Generated by Django 3.1.2 on 2020-12-04 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='paid_to',
            field=models.CharField(default='anon', max_length=40),
            preserve_default=False,
        ),
    ]
