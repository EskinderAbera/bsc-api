"""Performance_Management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('bsc/', include('bsc.urls')),
    path('bod/', include('bod.urls')),
    path('cooperative/', include('cooperative.urls')),
    path('corporate/', include('corporate.urls')),
    path('credit/', include('credit.urls')),
    path('finance/', include('finance.urls')),
    path('hc/', include('hc.urls')),
    path('ifb/', include('ifb.urls')),
    path('internal/', include('internal.urls')),
    path('is/', include('InformationSystem.urls')),
    path('legal/', include('legal.urls')),
    path('operation/', include('operation.urls')),
    path('risk/', include('risk.urls')),
    path('strategy/', include('strategy.urls')),
    path('tech/', include('tech.urls')),
    path('director/', include('director.urls'))
]
