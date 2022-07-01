from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

routes = SimpleRouter()

routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet,
                basename='auth-register')

urlpatterns = [
    *routes.urls,
    path('department/', department_list),    
    path('department/<str:pk>/', department_detail),  
    path('role/', role_list),
    path('role_detail/<str:pk>/', role_detail),
    path('auth/user/<str:pk>/', UserDetail.as_view()),
]
