from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
import uuid

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, password=None, **kwargs):
        # if not email:
        #     raise ValueError("Users must have an email address")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, username, password):
        user = self.model(
            username=username,
            password=password

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class Department(models.Model):
    dept_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dept_name = models.CharField(max_length=128, blank=False)

    def __str__(self):
        return f"{self.dept_name}"


class Role(models.Model):
    role_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role_name = models.CharField(max_length=128, blank=False)
    hierarchy = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.role_name}"


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, blank=False, unique=True)
    first_name = models.CharField(max_length=128, blank=False)
    last_name = models.CharField(max_length=128, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return f"{self.username}"


