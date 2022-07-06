from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
# from bod.models import KPI
# from cooperative.models import KPI
# from corporate.models import KPI
# from credit.models import KPI
# from finance.models import KPI
# from hc.models import KPI
# from ifb.models import KPI
# from internal.models import KPI
# from IS.models import KPI
# from legal.models import KPI
# from operation.models import KPI
# from risk.models import KPI
# from strategy.models import KPI
# from tech.models import KPI

# Create your views here.

@api_view(['GET', 'POST'])
def department_list(request):
    
    if request.method == 'GET':
        snippets = Department.objects.all()
        serializer = DepartmentSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DepartmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def department_detail(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DepartmentSerializer(department)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DepartmentSerializer(department, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        department.delete()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
def role_list(request):
    
    if request.method == 'GET':
        snippets = Role.objects.all()
        serializer = RoleSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RoleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def role_detail(request, pk):
    try:
        role = Role.objects.get(pk=pk)
    except Role.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RoleSerializer(role)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RoleSerializer(role, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        role.delete()
        return HttpResponse(status=204)


class LoginViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = LoginSerializers
    permission_classes = (AllowAny,)
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        serialized_data = serializer.validated_data
        user = User.objects.get(id = serialized_data['user']['id'])
        if(user.department.dept_name == "Banking Operations Scorecard"):
            kpis = user.bod_user.all()
        elif (user.department.dept_name == "Corporate Banking Process"):
            kpis = user.corporate_user.all()
        elif(user.department.dept_name == "Cooperative Banking Process"):
            kpis = user.cooperative_user.all()
        elif(user.department.dept_name == "Credit Appraisal and Portfolio Management"):
            kpis = user.credit_user.all()
        elif(user.department.dept_name == "Finance and Facilities Management Scorecard"):
            kpis = user.finance_user.all()
        elif(user.department.dept_name == "Human Capital and Projects Management Scorecard"):
            kpis = user.hc_user.all()
        elif(user.department.dept_name == "Internal Audit Process"):
            kpis = user.internal_user.all()
        elif(user.department.dept_name == "Interest Free Banking Process"):
            kpis = user.ifb_user.all()
        elif(user.department.dept_name == "Information System"):
            kpis = user.information_system_user.all()
        elif(user.department.dept_name == "Legal Services"):
            kpis = user.legal_user.all()
        elif(user.department.dept_name == "Board of Director Secretary"):
            kpis = user.bod_user.all()
        elif(user.department.dept_name == "Risk and Compliance Management Process"):
            kpis = user.risk_user.all()
        elif(user.department.dept_name == "Strategy and Marketing"):
            kpis = user.strategy_user.all()
        elif(user.department.dept_name == "Tech and Digital Banking Process"):
            kpis = user.tech_user.all()
        KPIS = []
        for kpi in kpis:
            actual_aggregate = kpi.January + kpi.February + kpi.March + kpi.April + kpi.May + kpi.June + kpi.July + kpi.August + kpi.September +  kpi.October + kpi.November + kpi.December
            serializer = KPISerializer(kpi)
            serialized_data = serializer.data
            serialized_data['actual_aggregate'] = actual_aggregate
            serialized_data['perspective_weight'] = kpi.perspective.perspective_weight
            serialized_data['objective_weight'] = kpi.objective.objective_weight
            KPIS.append(serialized_data)
        return Response(sorted(KPIS, key=lambda x: x['perspective']), status=status.HTTP_200_OK) 


class RegistrationViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        role = Role.objects.get(role_name = request.data.get("role"))
        department = Department.objects.get(dept_name = request.data.get("department"))
        request.data['department'] = department.dept_id
        request.data['role'] = role.role_id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        serialized_data = serializer.data
        serialized_data['role'] = role.role_name
        serialized_data['department'] = department.dept_name
        return Response(
            {
                "user": serialized_data,
                "refresh": res["refresh"],
                "token": res["access"],
            },
            status=status.HTTP_201_CREATED,
        )


class UserDetail(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = RegisterSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = RegisterSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserGroup(APIView):
    def get_object(self):
        try:
            return User.objects.all()
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = RegisterSerializer(user)
        return Response(serializer.data)
