# Generated by Django 4.0.5 on 2022-07-04 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perspective',
            fields=[
                ('perspective_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('perspective_name', models.CharField(max_length=120)),
                ('perspective_weight', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Objectives',
            fields=[
                ('objective_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('objective_name', models.CharField(max_length=120)),
                ('objective_weight', models.FloatField()),
                ('perspective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hc.perspective')),
            ],
        ),
        migrations.CreateModel(
            name='KPI',
            fields=[
                ('kpi_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('kpi_name', models.CharField(max_length=120)),
                ('kpi_weight', models.FloatField()),
                ('kpi_unit_measurement', models.CharField(choices=[('Percentage', 'Percentage'), ('ETB', 'ETB'), ('USD', 'USD'), ('Numbers', 'Numbers'), ('Levels', 'Levels')], default='Percentage', max_length=50, verbose_name='kpi_unit_measurement')),
                ('kpi_target', models.FloatField(blank=True)),
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
                ('objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hc.objectives')),
                ('perspective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hc.perspective')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hc_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
