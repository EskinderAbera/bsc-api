# Generated by Django 4.0.5 on 2022-06-10 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bsc', '0003_remove_objectives_month'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kpi',
            name='kpi_actual',
        ),
    ]
