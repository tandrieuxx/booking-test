from django import forms

from booking.models import Resource, Booking


class ResourceForm(forms.ModelForm):
    """
    Django form for the Resource model
    """

    class Meta:
        model = Resource
        fields = ["label", "type", "location", "capacity"]


class BookingForm(forms.ModelForm):
    """
    Django form for the Booking model
    """

    class Meta:
        model = Booking
        fields = ["title", "start_date", "end_date", "resource"]
