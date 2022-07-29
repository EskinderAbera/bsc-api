from dataclasses import fields
from pyexpat import model
from .models import KPI, Perspective
from rest_framework import serializers


class KPISerializer(serializers.Serializer):
    kpi_id = serializers.CharField(max_length = 120)
    objective = serializers.CharField(max_length=120)
    kpi_name = serializers.CharField(max_length=120)
    kpi_weight = serializers.FloatField()
    kpi_target = serializers.FloatField()
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
    January = serializers.FloatField()
    February = serializers.FloatField()
    March = serializers.FloatField()
    April = serializers.FloatField()
    May = serializers.FloatField()
    June = serializers.FloatField()
    July = serializers.FloatField()
    August = serializers.FloatField()
    September = serializers.FloatField()
    October = serializers.FloatField()
    November = serializers.FloatField()
    December = serializers.FloatField()
    is_active = serializers.BooleanField()


class PlanKPISerializer(serializers.Serializer):
    kpi_id = serializers.CharField(max_length = 120)
    perspective = serializers.CharField(max_length=120)
    objective = serializers.CharField(max_length=120)
    kpi_name = serializers.CharField(max_length=120)
    kpi_weight = serializers.FloatField()
    kpi_target = serializers.FloatField()
    kpi_unit_measurement = serializers.CharField(max_length=120)

class AddActualKPISerializer(serializers.ModelSerializer):
    class Meta:
        model = KPI
        fields = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    
class AddKPISerializer(serializers.ModelSerializer):
    class Meta:
        model = KPI
        fields = ['kpi_id','kpi_name', 'kpi_weight', 'kpi_target', 'perspective', 'objective', 'kpi_unit_measurement', 'user']
        

class ObjectiveSerializer(serializers.Serializer):
    perspective = serializers.CharField(max_length=120)
    objective_name = serializers.CharField(max_length=120)

class PerspectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perspective
        fields = '__all__'