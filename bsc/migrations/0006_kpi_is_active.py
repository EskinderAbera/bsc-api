# Generated by Django 4.0.5 on 2022-06-29 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsc', '0005_alter_kpi_april_alter_kpi_august_alter_kpi_december_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kpi',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
