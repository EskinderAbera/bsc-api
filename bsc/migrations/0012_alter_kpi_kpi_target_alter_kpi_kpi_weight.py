# Generated by Django 4.0.5 on 2022-07-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsc', '0011_alter_kpi_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi',
            name='kpi_target',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='kpi',
            name='kpi_weight',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
