from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from rest_framework import viewsets

from booking.forms import ResourceForm, BookingForm
from booking.models import Resource, Booking
from booking.serializers import UserSerializer, ResourceSerializer, BookingSerializer


# Pages


def index(request):
    # Home page listing resources and bookings
    context = {
        "resources": Resource.objects.all(),
        "bookings": Booking.objects.all(),
        "resource_form": ResourceForm(),
        "booking_form": BookingForm(),
    }
    return render(request, "booking/index.html", context)


def resource(request):
    # Resource form processing

    form = ResourceForm(request.POST)
    if form.is_valid():
        context = {"resource": form.save()}
        # Return a new component for the created resource

        return render(request, "booking/resource.html", context)


def booking(request):
    # Booking form processing

    form = BookingForm(request.POST)
    if form.is_valid():
        context = {"booking": form.save()}
        # Return a new component for the created booking
        return render(request, "booking/booking.html", context)


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
