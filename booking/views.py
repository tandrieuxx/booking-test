from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.utils import timezone
from rest_framework import viewsets

from booking.forms import BookingForm, ProfileForm, ResourceForm, SignupForm
from booking.models import Booking, Resource
from booking.serializers import BookingSerializer, ResourceSerializer, UserSerializer

# Website requests


@login_required
def index(request):
    # Home page listing resources and user's bookings

    # Admin can see all, users can see theirs only
    if request.user.has_perm("admin"):
        bookings = Booking.objects.all()
    else:
        bookings = Booking.objects.filter(user=request.user)

    context = {
        "resources": Resource.objects.all(),
        "bookings": bookings,
        "resource_form": ResourceForm(),
        "booking_form": BookingForm(),
        "now": timezone.now(),
    }
    return render(request, "booking/index.html", context)


@login_required
@permission_required("admin")
def resource(request):
    """Resource form processing"""

    # If an ID is provided then an existing resource is edited, otherwise a new one is created
    if request.POST.get("id", "") != "":
        res = get_object_or_404(Resource, id=int(request.POST["id"]))
        form = ResourceForm(request.POST, instance=res)
    else:
        form = ResourceForm(request.POST)

    if form.is_valid():
        # Return a new component for the created or edited resource
        context = {"resource": form.save()}
        template = loader.get_template("booking/resource.html")

        # 'success' is to tell frontend that a resource component is returned
        return JsonResponse({
            "success": True,
            "html": template.render(context, request)
        })

    # If form is invalid, return the form sub-template including errors
    context = {"resource_form": form}
    template = loader.get_template("booking/resource_form.html")

    # 'success' tells frontend that a form component is returned
    return JsonResponse({
        "success": False,
        "html": template.render(context, request)
    })


@login_required
@permission_required("admin")
def delete_resource(request):
    """Resource deletion"""

    id = request.POST.get("id")
    res = get_object_or_404(Resource, id=id)
    res.delete()

    return HttpResponse(status=204)


@login_required
def booking(request):
    """Booking form processing"""

    # If an ID is provided then an existing booking is edited, otherwise a new one is created
    if request.POST.get("id", "") != "":
        book = get_object_or_404(Booking, id=int(request.POST["id"]))
        if book.user == request.user:
            form = BookingForm(request.POST, instance=book)
        else:
            return HttpResponse(status=403)
    else:
        form = BookingForm(request.POST)

    if form.is_valid():
        # User is set to connected user
        book = form.save(commit=False)
        book.user = request.user
        book.save()

        # Return a new component for the created or edited booking
        context = {"booking": book}
        template = loader.get_template("booking/booking.html")

        # 'success' is to tell frontend that a booking component is returned
        return JsonResponse({
            "success": True,
            "html": template.render(context, request)
        })

    # If form is invalid, return the form sub-template including errors
    context = {"booking_form": form}
    template = loader.get_template("booking/booking_form.html")

    # 'success' tells frontend that a form component is returned
    return JsonResponse({
        "success": False,
        "html": template.render(context, request)
    })


@login_required
def delete_booking(request):
    """booking deletion"""

    id = request.POST.get("id")
    res = get_object_or_404(Booking, id=id)
    res.delete()

    return HttpResponse(status=204)


def signup(request):
    """Sign up a new user"""

    if request.method == "POST":
        form = SignupForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            # Save user info + profile info (for timezone and language)
            form.save()
            profile = profile_form.save(commit=False)
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            profile.user = user
            profile.save()

            login(request, user)
            return redirect("/")
    else:
        form = SignupForm()
        profile_form = ProfileForm()
    return render(
        request,
        "registration/signup.html",
        {"form": form, "profile_form": profile_form},
    )


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
