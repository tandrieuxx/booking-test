import pytz
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Resource(models.Model):
    """
    Represents a bookable resource (i.e. a meeting room)
    """

    # Resource types
    MEETING_ROOM = "MEET"
    CONFERENCE_ROOM = "CONF"
    WORKSHOP = "WORK"
    PROJECTOR = "PROJ"
    MISC = "MISC"
    TYPE_CHOICES = (
        (MEETING_ROOM, _("Meeting room")),
        (CONFERENCE_ROOM, _("Conference room")),
        (WORKSHOP, _("Workshop")),
        (PROJECTOR, _("Video projector")),
        (MISC, _("Others")),
    )

    label = models.CharField(_("Label"), max_length=100)
    type = models.CharField(_("Resource type"), max_length=4, choices=TYPE_CHOICES)
    location = models.CharField(_("Location"), max_length=200)
    capacity = models.IntegerField(_("Capacity"), default=0)

    def __str__(self):
        return self.label


class Booking(models.Model):
    """
    Represents a booking for a resource and a time range, by a user
    """

    title = models.CharField(_("Title"), max_length=100)
    start_date = models.DateTimeField(_("Start"))
    end_date = models.DateTimeField(_("End"))
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def check_overlap(cls, resource, start_date, end_date):
        """
        Check if a resource is booked during the given time range
        :param resource: Resource to check
        :param start_date: Start of the period to check
        :param end_date: End of the period to check
        :return: True if the resource is booked, False otherwise
        """

        bookings = cls.objects.filter(
            resource=resource, start_date__lte=end_date, end_date__gte=start_date
        )
        return len(bookings) > 0


class Profile(models.Model):
    """
    Model used to extend default User model
    """

    TIMEZONE_CHOICES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    FR = "fr"
    EN = "en"
    LANGUAGE_CHOICES = ((EN, "English"), (FR, "Français"))

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    timezone = models.CharField(
        _("Time zone"), max_length=50, choices=TIMEZONE_CHOICES, default="Europe/Paris",
    )
    language = models.CharField(
        _("Language"), max_length=10, choices=LANGUAGE_CHOICES, default=EN,
    )
