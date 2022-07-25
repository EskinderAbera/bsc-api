# Generated by Django 4.0.5 on 2022-07-25 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('strategy', '0002_alter_kpi_kpi_target_alter_kpi_kpi_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strategy_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
