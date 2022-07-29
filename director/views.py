from core.models import User, SubDepartment
from rest_framework.views import APIView
from .serializers import KPISerializer, AddActualKPISerializer, AddKPISerializer, PlanKPISerializer, PerspectiveSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import KPI, Objectives, Perspective
from django.http import Http404

# Create your views here.

class KPIAPIView(APIView):   
    def get(self, request, subdepartment, format=None):
        dept = SubDepartment.objects.get(name = subdepartment)
        user = User.objects.get(subdepartment=dept.id)
        kpis = user.director_user.all()
        KPIS = []
        for kpi in kpis:
            actual_aggregate = kpi.January + kpi.February + kpi.March + kpi.April + kpi.May + kpi.June + kpi.July + kpi.August + kpi.September +  kpi.October + kpi.November + kpi.December
            serializer = KPISerializer(kpi)
            serialized_data = serializer.data
            numberOfmonthsLeft = 0
            if(kpi.January<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.February<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.March<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.April<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.May<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.June<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.July<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.August<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.September<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.October<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.November<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.December<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            serialized_data['actual_aggregate'] = actual_aggregate
            serialized_data['numberOfmonthsLeft'] = numberOfmonthsLeft
            perspective = Perspective.objects.get(perspective_name = serialized_data['perspective'])
            objective = Objectives.objects.get(objective_name = serialized_data['objective'])
            serialized_data['perspective_weight'] = perspective.perspective_weight
            serialized_data['objective_weight'] = objective.objective_weight
            KPIS.append(serialized_data)
        return Response(sorted(KPIS, key=lambda x: x['perspective']))


class GetKPIAPIView(APIView):
    def get(self, request, format=None):
        kpis = KPI.objects.all()
        KPIS = []
        for kpi in kpis:
            if kpi.kpi_unit_measurement == "Percentage":
                kpi.kpi_weight = kpi.kpi_weight * 100
                kpi.kpi_target = round(float(kpi.kpi_target) * 100, 2)
                serializer = PlanKPISerializer(kpi)
                serialized_data = serializer.data
                KPIS.append(serialized_data)
            else:
                kpi.kpi_weight = kpi.kpi_weight * 100
                kpi.kpi_target = round(float(kpi.kpi_target), 2)
                serializer = PlanKPISerializer(kpi)
                serialized_data = serializer.data
                KPIS.append(serialized_data)
        return Response(sorted(KPIS, key=lambda x: x['kpi_name']))


class AddActualKPIAPIView(APIView):

    def get_object(self, name):
        try:
            return KPI.objects.get(kpi_name=name)
        except User.DoesNotExist:
            raise Http404

    def post(self, request, name, format=None):
        kpi = self.get_object(name)
        if kpi.kpi_unit_measurement == "Percentage":
            if request.data.get("January"):
               request.data["January"] = float(request.data.get("January"))/100
            elif request.data.get("February"):
                request.data["February"] = float(request.data.get("February"))/100
            elif request.data.get("March"):
                request.data["March"] = float(request.data.get("March"))/100
            elif request.data.get("April"):
                request.data["April"] = float(request.data.get("April"))/100
            elif request.data.get("May"):
                request.data["May"] = float(request.data.get("May"))/100
            elif request.data.get("June"):
                request.data["June"] = float(request.data.get("June"))/100
            elif request.data.get("July"):
                request.data["July"] = float(request.data.get("July"))/100
            elif request.data.get("August"):
                request.data["August"] = float(request.data.get("August"))/100
            elif request.data.get("September"):
                request.data["September"] = float(request.data.get("September"))/100
            elif request.data.get("October"):
                request.data["October"] = float(request.data.get("October"))/100
            elif request.data.get("November"):
                request.data["November"] = float(request.data.get("November"))/100
            elif request.data.get("December"):
                request.data["December"] = float(request.data.get("December"))/100
        serializer = AddActualKPISerializer(kpi, data=request.data)
        if serializer.is_valid():
            if float(request.data.get("January", kpi.January)) != kpi.January and  float(request.data.get("January", kpi.January)) > float(0) and float(kpi.January) > float(0):
                return Response({"Error": "You have already added Actual Value for January!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("February", kpi.February)) != float(kpi.February) and  float(request.data.get("February")) > float(0) and float(kpi.February) > float(0):
                return Response({"Error": "You have already added Actual Value for February!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("March", kpi.March)) != float(kpi.March) and  float(request.data.get("March")) > float(0) and float(kpi.March) > float(0):
                return Response({"Error": "You have already added Actual Value for March!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("April", kpi.April)) != float(kpi.April) and  float(request.data.get("April")) > float(0) and float(kpi.April) > float(0):
                return Response({"Error": "You have already added Actual Value for April!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("May", kpi.May)) != float(kpi.May) and  float(request.data.get("May")) > float(0) and float(kpi.May) > float(0):
                return Response({"Error": "You have already added Actual Value for May!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("June", kpi.June)) != float(kpi.June) and  float(request.data.get("June")) > float(0) and float(kpi.June) > float(0):
                return Response({"Error": "You have already added Actual Value for June!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("July", kpi.July)) != float(kpi.July) and  float(request.data.get("July")) > float(0) and float(kpi.July) > float(0):
                return Response({"Error": "You have already added Actual Value for July!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("August", kpi.August)) != float(kpi.August) and  float(request.data.get("August")) > float(0) and float(kpi.August) > float(0):
                return Response({"Error": "You have already added Actual Value for August!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("September", kpi.September)) != float(kpi.September) and  float(request.data.get("September")) > float(0) and float(kpi.September) > float(0):
                return Response({"Error": "You have already added Actual Value for September!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("October", kpi.October)) != float(kpi.October) and  float(request.data.get("October")) > float(0) and float(kpi.October) > float(0):
                return Response({"Error": "You have already added Actual Value for October!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("November", kpi.November)) != float(kpi.November) and  float(request.data.get("November")) > float(0) and float(kpi.November) > float(0):
                return Response({"Error": "You have already added Actual Value for November!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("December", kpi.December)) != float(kpi.December) and  float(request.data.get("December")) > float(0) and float(kpi.December) > float(0):
                return Response({"Error": "You have already added Actual Value for December!"}, status=status.HTTP_409_CONFLICT)
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
                user = User.objects.get(id = kpi.user)
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
                return Response({"Error": "KPI Does Not exist!"}, status=status.HTTP_404_NOT_FOUND)

class EditKPIAPIView(APIView):
   
    def post(self, request, name, format=None):
        try:
            kpi = KPI.objects.get(kpi_name=name)
            if kpi:
                user = User.objects.get(id = kpi.user)
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


class PerspectiveAPI(APIView):
    def get(self, request, format=None):
        kpis = Perspective.objects.all()
        serializer = PerspectiveSerializer(kpis, many=True)
    
        return Response(serializer.data)