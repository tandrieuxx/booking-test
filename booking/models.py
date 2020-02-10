from django.contrib.auth.models import User
from django.db import models


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
        (MEETING_ROOM, "Salle de réunion"),
        (CONFERENCE_ROOM, "Salle de conférence"),
        (WORKSHOP, "Atelier"),
        (PROJECTOR, "Projecteur vidéo"),
        (MISC, "Divers"),
    )

    label = models.CharField("Libellé", max_length=100)
    type = models.CharField("Type de ressource", max_length=4, choices=TYPE_CHOICES)
    location = models.CharField("Emplacement", max_length=200)
    capacity = models.IntegerField("Capacité d'accueil", default=0)


class Booking(models.Model):
    """
    Represents a booking for a resource and a time range, by a user
    """

    title = models.CharField("Objet", max_length=100)
    start_date = models.DateTimeField("Début")
    end_date = models.DateTimeField("Fin")
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
