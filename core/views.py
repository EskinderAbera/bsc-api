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
from django.contrib.auth import authenticate

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
        if(user.department.dept_name == "admin" and user.subdepartment == None):
            kpis = user.ceo_user.all()
        elif(user.department.dept_name == "Banking Operations Scorecard" and user.subdepartment == None):
            kpis = user.operation_user.all()
        elif (user.department.dept_name == "Corporate Banking Process" and user.subdepartment == None):
            kpis = user.corporate_user.all()
        elif(user.department.dept_name == "Cooperative Banking Process" and user.subdepartment == None):
            kpis = user.cooperative_user.all()
        elif(user.department.dept_name == "Credit Appraisal and Portfolio Management" and user.subdepartment == None):
            kpis = user.credit_user.all()
        elif(user.department.dept_name == "Finance and Facilities Management Scorecard" and user.subdepartment == None):
            kpis = user.finance_user.all()
        elif(user.department.dept_name == "Human Capital and Projects Management Scorecard" and user.subdepartment == None):
            kpis = user.hc_user.all()
        elif(user.department.dept_name == "Internal Audit Process" and user.subdepartment == None):
            kpis = user.internal_user.all()
        elif(user.department.dept_name == "Interest Free Banking Process" and user.subdepartment == None):
            kpis = user.ifb_user.all()
        elif(user.department.dept_name == "Information System" and user.subdepartment == None):
            kpis = user.information_system_user.all()
        elif(user.department.dept_name == "Legal Services" and user.subdepartment == None):
            kpis = user.legal_user.all()
        elif(user.department.dept_name == "Board of Director Secretary" and user.subdepartment == None):
            kpis = user.bod_user.all()
        elif(user.department.dept_name == "Risk and Compliance Management Process" and user.subdepartment == None):
            kpis = user.risk_user.all()
        elif(user.department.dept_name == "Strategy and Marketing" and user.subdepartment == None):
            kpis = user.strategy_user.all()
        elif(user.department.dept_name == "Tech and Digital Banking Process" and user.subdepartment == None):
            kpis = user.tech_user.all()
        else:
            kpis = user.director_user.all()
        KPIS = []
        for kpi in kpis:
            actual_aggregate = kpi.January + kpi.February + kpi.March + kpi.April + kpi.May + kpi.June + kpi.July + kpi.August + kpi.September +  kpi.October + kpi.November + kpi.December
            serializer = KPISerializer(kpi)
            serialized_data = serializer.data
            numberOfmonthsLeft = 0

            if(kpi.January<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
                print(numberOfmonthsLeft)
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
            serialized_data['perspective_weight'] = kpi.perspective.perspective_weight
            serialized_data['objective_weight'] = kpi.objective.objective_weight
            serialized_data['numberOfmonthsLeft'] = numberOfmonthsLeft
            KPIS.append(serialized_data)
        return Response(sorted(KPIS, key=lambda x: x['perspective']), status=status.HTTP_200_OK) 


class RegistrationViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        role = Role.objects.get(role_name = request.data.get("role"))
        department = Department.objects.get(dept_name = request.data.get("department"))
        subdepartment = SubDepartment.objects.get(name = request.data.get("subdepartment"))
        request.data['department'] = department.dept_id
        request.data['role'] = role.role_id
        request.data['subdepartment'] = subdepartment.id
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
        serialized_data['subdepartment'] = subdepartment.name

        return Response(
            {
                "user": serialized_data,
                "refresh": res["refresh"],
                "token": res["access"],
            },
            status=status.HTTP_201_CREATED,
        )


class OtherLogin(APIView):
    def post(self, request, format=None):
        user = User.objects.get(username = request.data.get("username"))
        if user:
            username = request.data.get("username")
            password = request.data.get("password")
            authenticate(username=username, password=password)
            return Response({"Success"}, status=status.HTTP_200_OK)
        else:
            return Response({"Error":"User Does Not Exist!"}, status=status.HTTP_404_NOT_FOUND)


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
