# Generated by Django 3.1.2 on 2020-10-27 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0004_auto_20201022_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academicinternship',
            name='actual_fees',
        ),
        migrations.RemoveField(
            model_name='academicinternship',
            name='backend',
        ),
        migrations.RemoveField(
            model_name='academicinternship',
            name='frontend',
        ),
        migrations.RemoveField(
            model_name='academicworkshop',
            name='actual_fees',
        ),
        migrations.RemoveField(
            model_name='academicworkshop',
            name='backend',
        ),
        migrations.RemoveField(
            model_name='academicworkshop',
            name='frontend',
        ),
        migrations.RemoveField(
            model_name='cognitiveinternship',
            name='actual_fees',
        ),
        migrations.RemoveField(
            model_name='cognitiveinternship',
            name='backend',
        ),
        migrations.RemoveField(
            model_name='cognitiveinternship',
            name='frontend',
        ),
        migrations.RemoveField(
            model_name='cognitiveinternship',
            name='no_of_months',
        ),
        migrations.RemoveField(
            model_name='cognitiveworkshop',
            name='actual_fees',
        ),
        migrations.RemoveField(
            model_name='cognitiveworkshop',
            name='backend',
        ),
        migrations.RemoveField(
            model_name='cognitiveworkshop',
            name='frontend',
        ),
        migrations.RemoveField(
            model_name='employeeinternship',
            name='actual_fees',
        ),
        migrations.RemoveField(
            model_name='employeeinternship',
            name='backend',
        ),
        migrations.RemoveField(
            model_name='employeeinternship',
            name='frontend',
        ),
        migrations.RemoveField(
            model_name='employeeinternship',
            name='no_of_months',
        ),
    ]
