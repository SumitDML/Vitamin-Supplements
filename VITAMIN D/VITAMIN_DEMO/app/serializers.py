from rest_framework import serializers
from .models import *


class SunshineAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SunshineAvailability
        # fields = "__all__"
        fields = ['Month', 'Strength']


class ZoneSerializer(serializers.ModelSerializer):
    strengths = SunshineAvailabilitySerializer(many=True, read_only=True)

    class Meta:
        model = Zones
        fields = ['ZoneID', 'LatitudeMin', 'LatitudeMax', 'NorthSouth', 'strengths']


class ZoneViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zones
        fields = ['ZoneID', 'LatitudeMin', 'LatitudeMax', 'NorthSouth']


class ZipCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZipCodes
        fields = "__all__"


class TabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tabs
        fields = ['tab_id', 'name', 'display_name']


class TabChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = TabChild
        fields = ['tab_child_id', 'name', 'display_name']
