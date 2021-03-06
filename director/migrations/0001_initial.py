# Generated by Django 4.0.5 on 2022-07-29 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perspective',
            fields=[
                ('perspective_id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('perspective_name', models.CharField(max_length=120)),
                ('perspective_weight', models.FloatField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Objectives',
            fields=[
                ('objective_id', models.BigAutoField(auto_created=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('objective_name', models.CharField(max_length=120)),
                ('objective_weight', models.FloatField()),
                ('perspective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='director.perspective')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='KPI',
            fields=[
                ('kpi_id', models.BigAutoField(auto_created=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('kpi_name', models.CharField(max_length=120)),
                ('kpi_target', models.FloatField(blank=True, default=0)),
                ('kpi_weight', models.FloatField(blank=True, default=0)),
                ('kpi_unit_measurement', models.CharField(choices=[('Percentage', 'Percentage'), ('ETB', 'ETB'), ('USD', 'USD'), ('Numbers', 'Numbers'), ('Levels', 'Levels')], default='Percentage', max_length=50, verbose_name='kpi_unit_measurement')),
                ('January', models.FloatField(blank=True, default=0)),
                ('February', models.FloatField(blank=True, default=0)),
                ('March', models.FloatField(blank=True, default=0)),
                ('April', models.FloatField(blank=True, default=0)),
                ('May', models.FloatField(blank=True, default=0)),
                ('June', models.FloatField(blank=True, default=0)),
                ('July', models.FloatField(blank=True, default=0)),
                ('August', models.FloatField(blank=True, default=0)),
                ('September', models.FloatField(blank=True, default=0)),
                ('October', models.FloatField(blank=True, default=0)),
                ('November', models.FloatField(blank=True, default=0)),
                ('December', models.FloatField(blank=True, default=0)),
                ('Score_January', models.FloatField(blank=True, default=0)),
                ('Score_February', models.FloatField(blank=True, default=0)),
                ('Score_March', models.FloatField(blank=True, default=0)),
                ('Score_April', models.FloatField(blank=True, default=0)),
                ('Score_May', models.FloatField(blank=True, default=0)),
                ('Score_June', models.FloatField(blank=True, default=0)),
                ('Score_July', models.FloatField(blank=True, default=0)),
                ('Score_August', models.FloatField(blank=True, default=0)),
                ('Score_September', models.FloatField(blank=True, default=0)),
                ('Score_October', models.FloatField(blank=True, default=0)),
                ('Score_November', models.FloatField(blank=True, default=0)),
                ('Score_December', models.FloatField(blank=True, default=0)),
                ('aggregate', models.FloatField(blank=True, default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='director.objectives')),
                ('perspective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='director.perspective')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
