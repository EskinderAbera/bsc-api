from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('kpi/', KPIAPIView),
]
urlpatterns = format_suffix_patterns(urlpatterns)
