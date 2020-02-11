from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from rest_framework import viewsets

from booking.models import Resource, Booking
from booking.serializers import UserSerializer, ResourceSerializer, BookingSerializer


# Pages

def index(request):
    context = {
        "resources": Resource.objects.all(),
        "bookings": Booking.objects.all(),
    }
    return render(request, "booking/index.html", context)


# API endpoints

class ResourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows resources to be viewed or edited.
    """

    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bookings to be viewed or edited.
    """

    queryset = Booking.objects.all().order_by("-start_date")
    serializer_class = BookingSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
