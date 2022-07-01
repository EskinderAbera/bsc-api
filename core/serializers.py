from rest_framework import serializers
from .models import *
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['dept_id','dept_name']


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['role_id', 'role_name', 'hierarchy']


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "is_active",
            "department",
            "role"
        ]
        read_only_field = ["is_active"]


class RegisterSerializer(UserSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True, required=True
    )
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "password",
            "username",
            "is_active"
        ]

    def create(self, validated_data):
        try:
            user = User.objects.get(
                username=validated_data["username"])
        except ObjectDoesNotExist:
            user = User.objects.create_user(**validated_data)
            return user
        else:
            return user


class LoginSerializers(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["user"] = UserSerializer(self.user).data
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data