from core.models import User
from rest_framework.views import APIView
from .serializers import KPISerializer, AddActualKPISerializer, AddKPISerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import KPI, Objectives, Perspective
from django.http import Http404

# Create your views here.

class KPIAPIView(APIView):   
    def get(self, request, format=None):
        kpis = KPI.objects.all()
        KPIS = []
        for kpi in kpis:
            actual_aggregate = kpi.January + kpi.February + kpi.March + kpi.April + kpi.May + kpi.June + kpi.July + kpi.August + kpi.September +  kpi.October + kpi.November + kpi.December
            serializer = KPISerializer(kpi)
            serialized_data = serializer.data
            serialized_data['actual_aggregate'] = actual_aggregate
            KPIS.append(serialized_data)
        return Response(sorted(KPIS, key=lambda x: x['kpi_name']))


class AddActualKPIAPIView(APIView):

    def get_object(self, name):
        try:
            return KPI.objects.get(kpi_name=name)
        except User.DoesNotExist:
            raise Http404

    def put(self, request, name, format=None):
        kpi = self.get_object(name)
        serializer = AddActualKPISerializer(kpi, data=request.data)
        if serializer.is_valid():
            if float(request.data.get("January", kpi.January)) != kpi.January and  float(request.data.get("January", kpi.January)) > float(0) and float(kpi.January) > float(0):
                return Response({"Error": "You have already added Actual Value for January!"})
            elif float(request.data.get("February", kpi.February)) != float(kpi.February) and  float(request.data.get("February")) > float(0) and float(kpi.February) > float(0):
                return Response({"Error": "You have already added Actual Value for February!"})
            elif float(request.data.get("March", kpi.March)) != float(kpi.March) and  float(request.data.get("March")) > float(0) and float(kpi.March) > float(0):
                return Response({"Error": "You have already added Actual Value for March!"})
            elif float(request.data.get("April", kpi.April)) != float(kpi.April) and  float(request.data.get("April")) > float(0) and float(kpi.April) > float(0):
                return Response({"Error": "You have already added Actual Value for April!"})
            elif float(request.data.get("May", kpi.May)) != float(kpi.May) and  float(request.data.get("May")) > float(0) and float(kpi.May) > float(0):
                return Response({"Error": "You have already added Actual Value for May!"})
            elif float(request.data.get("June", kpi.June)) != float(kpi.June) and  float(request.data.get("June")) > float(0) and float(kpi.June) > float(0):
                return Response({"Error": "You have already added Actual Value for June!"})
            elif float(request.data.get("July", kpi.July)) != float(kpi.July) and  float(request.data.get("July")) > float(0) and float(kpi.July) > float(0):
                return Response({"Error": "You have already added Actual Value for July!"})
            elif float(request.data.get("August", kpi.August)) != float(kpi.August) and  float(request.data.get("August")) > float(0) and float(kpi.August) > float(0):
                return Response({"Error": "You have already added Actual Value for August!"})
            elif float(request.data.get("September", kpi.September)) != float(kpi.September) and  float(request.data.get("September")) > float(0) and float(kpi.September) > float(0):
                return Response({"Error": "You have already added Actual Value for September!"})
            elif float(request.data.get("October", kpi.October)) != float(kpi.October) and  float(request.data.get("October")) > float(0) and float(kpi.October) > float(0):
                return Response({"Error": "You have already added Actual Value for October!"})
            elif float(request.data.get("November", kpi.November)) != float(kpi.November) and  float(request.data.get("November")) > float(0) and float(kpi.November) > float(0):
                return Response({"Error": "You have already added Actual Value for November!"})
            elif float(request.data.get("December", kpi.December)) != float(kpi.December) and  float(request.data.get("December")) > float(0) and float(kpi.December) > float(0):
                return Response({"Error": "You have already added Actual Value for December!"})
            else:
                serializer.save()
                kpi.Score_January = ((kpi.January/kpi.kpi_target)*100) * kpi.kpi_weight
                kpi.Score_February = ((kpi.February/kpi.kpi_target)*100) * kpi.kpi_weight
                kpi.Score_March = ((kpi.March/kpi.kpi_target)*100) * kpi.kpi_weight
                kpi.Score_April = ((kpi.April/kpi.kpi_target)*100) * kpi.kpi_weight
                kpi.Score_May = ((kpi.May/kpi.kpi_target)*100) * kpi.kpi_weight
                kpi.Score_June = ((kpi.June/kpi.kpi_target)*100) * kpi.kpi_weight
                kpi.Score_July = ((kpi.July/kpi.kpi_target)*100) * kpi.kpi_weight
                kpi.Score_August = ((kpi.August/kpi.kpi_target)*100) * kpi.kpi_weight
                kpi.Score_September = ((kpi.September/kpi.kpi_target)*100) * kpi.kpi_weight
                kpi.Score_October = ((kpi.October/kpi.kpi_target)*100) * kpi.kpi_weight
                kpi.Score_November = ((kpi.November/kpi.kpi_target)*100) * kpi.kpi_weight
                kpi.Score_December = ((kpi.December/kpi.kpi_target)*100) * kpi.kpi_weight
                kpi.aggregate = kpi.Score_January + kpi.Score_February + kpi.Score_March + kpi.Score_April + kpi.Score_May + kpi.Score_June + kpi.Score_July + kpi.Score_August + kpi.Score_September +  kpi.Score_October + kpi.Score_November + kpi.Score_December
                kpi.save()
                serializer = KPISerializer(kpi)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddKPIView(APIView):
    def post(self, request, format=None):
        try:
            kpi = KPI.objects.get(kpi_name = request.data.get("kpi_name"))
            if kpi:
                return Response({"Error": "KPI already exist!"}, status=status.HTTP_409_CONFLICT)
        except KPI.DoesNotExist:
            perspective = Perspective.objects.get(perspective_name = request.data.get("perspective", ""))
            request.data['perspective'] = perspective.perspective_id
            objective = Objectives.objects.get(objective_name = request.data.get("objective", ""))
            request.data['objective'] = objective.objective_id
            user = User.objects.get(username = "admin")
            request.data['user'] = user.id
            serializer = AddKPISerializer(data=request.data)
            if serializer.is_valid():
                if serializer.validated_data['kpi_unit_measurement'] == "Percentage":
                    serializer.validated_data['kpi_weight'] = float(serializer.validated_data['kpi_weight'])/100
                    serializer.validated_data['kpi_target'] = float(serializer.validated_data['kpi_target'])/100
                    serializer.save()
                    serialized_data = serializer.data
                    serialized_data['perspective'] = perspective.perspective_name
                    serialized_data['objective'] = objective.objective_name
                    return Response(serialized_data, status=status.HTTP_201_CREATED)
                elif serializer.validated_data['kpi_unit_measurement'] == "ETB" or serializer.validated_data['kpi_unit_measurement'] == "USD" or serializer.validated_data['kpi_unit_measurement'] =="Numbers":
                    serializer.validated_data['kpi_weight'] = float(serializer.validated_data['kpi_weight'])/100
                    serializer.save()
                    serialized_data = serializer.data
                    serialized_data['perspective'] = perspective.perspective_name
                    serialized_data['objective'] = objective.objective_name
                return Response(serialized_data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditKPIAPIView(APIView):
   
    def put(self, request, name, format=None):
        try:
            kpi = KPI.objects.get(kpi_name=name)
            if kpi:
                user = User.objects.get(username = "admin")
                request.data['user'] = user.id
                perspective = Perspective.objects.get(perspective_name = request.data['perspective'])
                request.data['perspective'] = perspective.perspective_id
                objective = Objectives.objects.get(objective_name = request.data['objective'])
                request.data['objective'] = objective.objective_id
                serializer = AddKPISerializer(kpi, data=request.data)
                if serializer.is_valid():
                    if serializer.validated_data['kpi_unit_measurement'] == "Percentage":
                        serializer.validated_data['kpi_weight'] = float(serializer.validated_data['kpi_weight'])/100
                        serializer.validated_data['kpi_target'] = float(serializer.validated_data['kpi_target'])/100
                        serializer.save()
                        serialized_data = serializer.data
                        serialized_data['perspective'] = perspective.perspective_name
                        serialized_data['objective'] = objective.objective_name
                        serialized_data['user'] = user.username
                        return Response(serialized_data, status=status.HTTP_200_OK)
                    elif serializer.validated_data['kpi_unit_measurement'] == "ETB" or serializer.validated_data['kpi_unit_measurement'] == "USD" or serializer.validated_data['kpi_unit_measurement'] =="Numbers":
                        serializer.validated_data['kpi_weight'] = float(serializer.validated_data['kpi_weight'])/100
                        serializer.save()
                        serialized_data = serializer.data
                        serialized_data['perspective'] = perspective.perspective_name
                        serialized_data['objective'] = objective.objective_name
                        serialized_data['user'] = user.username
                        return Response(serialized_data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except KPI.DoesNotExist:
            return Response({"Error": "KPI does not exist!"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, name, format=None):
        try:
            kpi = KPI.objects.get(kpi_name = name)
            if kpi:
                return Response({"Status": "Success"}, status=status.HTTP_200_OK)
        except KPI.DoesNotExist:
            return Response({"Error": "KPI Does Not Exist!"}, status=status.HTTP_404_NOT_FOUND)


class ObjectiveAPI(APIView):   
    def get(self, request, format=None):

        dicti = [{"Financial": {"Increase Profitability",
                               "Enhance Market Share",
                               "Enhance Financial Resources Mobilization",
                               "Enhance Financial Soundness"
                               }},
                 {"Customer": {"Increase Customer Satisfaction",
                               "Increase Customer Acquisition (customer base)",
                               "Improve customer retention"
                              }},
                 {"Internal Business Process": {"Enhance process efficiency and effectiveness",
                                                "Improve risk and internal control management",
                                                "Improve marketing of the bank"
                                                }},
                 {"Learning and Growth": {"Enhance Human Capital",
                                          "Enhance Organizational",
                                          "Enhance Information System Capital"
                                          }}          
                ]
        return Response(data=dicti)