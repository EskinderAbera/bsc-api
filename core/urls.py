from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

routes = SimpleRouter()

routes.register(r'auth/register', RegisterAPIView,
                basename='auth-register')

urlpatterns = [
    # *routes.urls,
    path('department/', department_list),    
    path('department/<str:pk>/', department_detail),  
    path('role/', role_list),
    path('role_detail/<str:pk>/', role_detail),
    path('auth/register/', RegisterAPIView.as_view()),
    path('auth/user/<str:pk>/', UserDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
