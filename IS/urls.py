from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('kpi/', KPIAPIView.as_view()),
    path('objective/', ObjectiveAPI.as_view()),
    path('add/actual/kpi/<str:name>/', AddActualKPIAPIView.as_view()),
    path('add/kpi/', AddKPIView.as_view()),
    path('edit/kpi/<str:name>/', EditKPIAPIView.as_view()),
    path('planning/kpi/', GetKPIAPIView.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
