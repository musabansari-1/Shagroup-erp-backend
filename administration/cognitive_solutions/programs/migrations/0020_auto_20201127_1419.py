# Generated by Django 3.1.2 on 2020-11-27 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0019_auto_20201127_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academicinternship',
            name='internship',
        ),
        migrations.RemoveField(
            model_name='cognitiveinternship',
            name='internship',
        ),
        migrations.RemoveField(
            model_name='employeeinternship',
            name='internship',
        ),
        migrations.AddField(
            model_name='academicinternship',
            name='batch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='programs.batch'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cognitiveinternship',
            name='batch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='programs.batch'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employeeinternship',
            name='batch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='programs.batch'),
            preserve_default=False,
        ),
    ]