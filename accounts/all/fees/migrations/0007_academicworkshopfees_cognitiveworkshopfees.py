# Generated by Django 3.1.2 on 2020-11-30 18:04

import accounts.all.fees.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0020_auto_20201127_1419'),
        ('fees', '0006_auto_20201127_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='CognitiveWorkshopFees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_no', models.CharField(editable=False, max_length=10, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.PositiveIntegerField()),
                ('mode_of_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fees.paymenttype')),
                ('received_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programs.cognitiveworkshop')),
            ],
            options={
                'abstract': False,
            },
            bases=(accounts.all.fees.models.WorkshopFeesCleanMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AcademicWorkshopFees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_no', models.CharField(editable=False, max_length=10, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.PositiveIntegerField()),
                ('mode_of_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fees.paymenttype')),
                ('received_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programs.academicworkshop')),
            ],
            options={
                'abstract': False,
            },
            bases=(accounts.all.fees.models.WorkshopFeesCleanMixin, models.Model),
        ),
    ]