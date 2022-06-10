from calendar import month
from django.shortcuts import render
from core.models import User
from rest_framework.views import APIView
from .serializers import KPISerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import KPI, Objectives

# Create your views here.

class Kpi(generics.GenericAPIView):
    serializer_class = KPISerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            kpi_unit_measurement = request.data.get("kpi_unit_measurement", "")
            kpi_target = request.data.get("kpi_target", "")
            kpi_weight = request.data.get("kpi_weight", "")
            objective_id = request.data.get("objective", "")
            kpi_actual = request.data.get("kpi_actual", "")
            kpi_name = request.data.get("kpi_name", "")
            user = User.objects.get(id = request.data.get("user", ""))
            if kpi_unit_measurement=='Percentage':
                kpi_target = float(kpi_target)/100
                kpi_weight = float(kpi_weight)/100
                kpi_actual = float(kpi_actual)/100
                kpi_score = (kpi_actual_percent * kpi_weight) * 100
                kpi = KPI.objects.create(kpi_name = kpi_name, kpi_weight=kpi_weight, 
                                            kpi_unit_measurement=kpi_unit_measurement, kpi_target=kpi_target, 
                                            objective_id = objective_id, user = user, kpi_actual = kpi_actual, 
                                            kpi_actual_percent=kpi_actual_percent, kpi_score=kpi_score)
                return Response(serializer.data, status=status.HTTP_200_OK)

            elif kpi_unit_measurement == 'ETB' & kpi_unit_measurement == 'USD' & kpi_unit_measurement == 'Number':
                kpi_actual_percent = kpi_actual/kpi_target
                kpi_score = kpi_actual_percent * kpi_weight
                kpi = KPI.objects.create(kpi_name = kpi_name, kpi_weight=kpi_weight, 
                                            kpi_unit_measurement=kpi_unit_measurement, kpi_target=kpi_target, 
                                            objective_id = objective_id, user = user, kpi_actual = kpi_actual, month=month, 
                                            kpi_actual_percent=kpi_actual_percent, kpi_score=kpi_score)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KPIAPIView(APIView):   
    def get(self, request, format=None):
        kpis = KPI.objects.all()
        serializer = KPISerializer(kpis, many=True)
        return Response(serializer.data)
        




            
            

        
        
        