from django.contrib import admin
from django.contrib.auth import views as auth_views
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
    path('accounts/', include('django.contrib.auth.urls')),
]
