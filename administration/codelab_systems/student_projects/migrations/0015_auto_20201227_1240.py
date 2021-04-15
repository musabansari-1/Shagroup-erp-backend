# Generated by Django 3.1.2 on 2020-12-27 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0026_auto_20201227_1235'),
        ('student_projects', '0014_auto_20201204_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='backend',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='programs.backend'),
        ),
        migrations.AlterField(
            model_name='project',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='programs.company'),
        ),
        migrations.AlterField(
            model_name='project',
            name='frontend',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='programs.frontend'),
        ),
        migrations.AlterField(
            model_name='project',
            name='trainer_1_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student_projects.trainer'),
        ),
        migrations.AlterField(
            model_name='project',
            name='trainer_1_role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student_projects.trainerrole'),
        ),
        migrations.AlterField(
            model_name='project',
            name='trainer_2_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trainer_2', to='student_projects.trainer'),
        ),
        migrations.AlterField(
            model_name='project',
            name='trainer_2_role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trainer_2_role', to='student_projects.trainerrole'),
        ),
        migrations.AlterField(
            model_name='studentproject',
            name='college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='programs.college'),
        ),
        migrations.AlterField(
            model_name='studentproject',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='programs.course'),
        ),
        migrations.AlterField(
            model_name='studentproject',
            name='degree',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='degree', to='programs.college'),
        ),
        migrations.AlterField(
            model_name='studentproject',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student_projects.project'),
        ),
        migrations.AlterField(
            model_name='studentproject',
            name='puc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student_projects.puc'),
        ),
        migrations.AlterField(
            model_name='studentproject',
            name='sslc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student_projects.sslc'),
        ),
        migrations.AlterField(
            model_name='studentproject',
            name='stream',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='programs.stream'),
        ),
    ]