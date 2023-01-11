from rest_framework import serializers
from .models import *


class ZoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zones
        fields = "__all__"


class SunshineAvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = SunshineAvailability
        fields = "__all__"


class ZipCodesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ZipCodes
        fields = "__all__"
