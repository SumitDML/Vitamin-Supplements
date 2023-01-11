from rest_framework import serializers
from .models import *


class ZoneSerializer(serializers.HyperlinkedModelSerializer):
    zoneID = serializers.ReadOnlyField()

    class Meta:
        model = Zones
        fields = "__all__"


class SunshineAvailabilitySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = SunshineAvailability
        fields = "__all__"


class ZipCodesSerializer(serializers.HyperlinkedModelSerializer):
    zipCode = serializers.ReadOnlyField()

    class Meta:
        model = ZipCodes
        fields = "__all__"
