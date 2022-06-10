from dataclasses import fields
from pyexpat import model
from .models import KPI, Objectives
from rest_framework import serializers


class KPISerializer(serializers.Serializer):
    objective = serializers.CharField(max_length=120)
    kpi_name = serializers.CharField(max_length=120)
    perspective = serializers.CharField(max_length=120)
    kpi_unit_measurement = serializers.CharField(max_length=120)
    Score_January = serializers.FloatField()
    Score_February = serializers.FloatField()
    Score_March = serializers.FloatField()
    Score_April = serializers.FloatField()
    Score_May = serializers.FloatField()
    Score_June = serializers.FloatField()
    Score_July = serializers.FloatField()
    Score_August = serializers.FloatField()
    Score_September = serializers.FloatField()
    Score_October = serializers.FloatField()
    Score_November = serializers.FloatField()
    Score_December = serializers.FloatField()
    aggregate = serializers.FloatField()
    