# Generated by Django 4.0.5 on 2022-07-04 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bsc', '0008_rename_vp_bod_weight_perspective_vp_bod_perspective_weight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kpi', to=settings.AUTH_USER_MODEL),
        ),
    ]
