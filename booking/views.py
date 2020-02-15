from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

from booking.forms import ResourceForm, BookingForm
from booking.models import Resource, Booking
from booking.serializers import UserSerializer, ResourceSerializer, BookingSerializer


# Website requests

@login_required
def index(request):
    # Home page listing resources and bookings
    context = {
        "resources": Resource.objects.all(),
        "bookings": Booking.objects.all(),
        "resource_form": ResourceForm(),
        "booking_form": BookingForm(),
    }
    return render(request, "booking/index.html", context)


@login_required
def resource(request):
    # Resource form processing

    # If an ID is provided then an existing resource is edited, otherwise a new one is created
    if request.POST.get("id", "") != "":
        res = get_object_or_404(Resource, id=int(request.POST["id"]))
        form = ResourceForm(request.POST, instance=res)
    else:
        form = ResourceForm(request.POST)

    if form.is_valid():
        context = {"resource": form.save()}

        # Return a new component for the created or edited resource
        return render(request, "booking/resource.html", context)

    # TODO : Handle invalid form


@login_required
def delete_resource(request):
    # Resource deletion

    id = request.POST.get("id")
    res = get_object_or_404(Resource, id=id)
    res.delete()

    return HttpResponse(status=204)


@login_required
def booking(request):
    # Booking form processing

    # If an ID is provided then an existing booking is edited, otherwise a new one is created
    if request.POST.get("id", "") != "":
        book = get_object_or_404(Booking, id=int(request.POST["id"]))
        form = BookingForm(request.POST, instance=book)
    else:
        form = BookingForm(request.POST)

    if form.is_valid():
        context = {"booking": form.save()}

        # Return a new component for the created or edited booking
        return render(request, "booking/booking.html", context)

    # TODO : Handle invalid form


@login_required
def delete_booking(request):
    # booking deletion

    id = request.POST.get("id")
    res = get_object_or_404(Booking, id=id)
    res.delete()

    return HttpResponse(status=204)


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
