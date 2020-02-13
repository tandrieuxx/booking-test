"""booking_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework import routers

from booking import views

# API Routes
router = routers.DefaultRouter()
router.register(r"resource", views.ResourceViewSet)
router.register(r"booking", views.BookingViewSet)
router.register(r"users", views.UserViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("", views.index, name="index"),
    path("resource", views.resource, name="resource"),
    path("delete_resource", views.delete_resource, name="delete_resource"),
    path("booking", views.booking, name="booking"),
    path("delete_booking", views.delete_booking, name="delete_booking"),
]
