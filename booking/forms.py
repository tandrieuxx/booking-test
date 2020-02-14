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

    start_date = forms.DateTimeField(
        input_formats=["%d/%m/%Y %H:%M"],
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control datetimepicker-input",
                "data-target": "#id_start_date",
                "data-toggle": "datetimepicker",
            }
        ),
    )
    end_date = forms.DateTimeField(
        input_formats=["%d/%m/%Y %H:%M"],
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control datetimepicker-input",
                "data-target": "#id_end_date",
                "data-toggle": "datetimepicker",
            }
        ),
    )

    class Meta:
        model = Booking
        fields = ["title", "start_date", "end_date", "resource"]
