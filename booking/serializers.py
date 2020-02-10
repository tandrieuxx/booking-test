from django.contrib.auth.models import User
from rest_framework import serializers

from booking.models import Resource


class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ["label", "type", "location", "capacity"]


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ["title", "start_date", "end_date", "resource", "user"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
