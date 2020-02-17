from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

from booking.models import Booking, Profile, Resource


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

    def clean(self):
        """
        Custom form validation
        """
        cleaned_data = super().clean()

        # Check if the edited or created booking is not in the past (or currently effective)
        if timezone.now() > cleaned_data.get("start_date"):
            raise ValidationError(
                "Start date cannot be in the past", code="start_date_past"
            )


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["timezone"]
