import enum

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


# class Vitamins(enum.Enum):
#     Vitamin_A = 1
#     Vitamin_B = 2
#     Vitamin_C = 3
#     Vitamin_D = 4


# Create your views here.
# vitamin_types = (
#     (1, "Vitamin_A"),
#     (2, "Vitamin_B"),
#     (3, "Vitamin_C"),
#     (4, "Vitamin_D"),
# )


@api_view(['GET'])
def view_data(request):
    vitamin = request.GET['keyword']
    try:

        zones = Zones.objects.filter(vitamin_type=vitamin)
        strength = SunshineAvailability.objects.filter(vitamin_type=vitamin)
        serializer = ZoneViewSerializer(zones, many=True, context={'request': request})
        serializer2 = SunshineAvailabilitySerializer(strength, many=True, context={'request': request})
        return Response({
            'status': True,
            'message': "Fetched Successfully!!",
            'zones': serializer.data,
            'strengths': serializer2.data
        })
    except Exception as e:
        print(e)
    return Response({
        'status': True,
        'message': "Error Occured!",
        # 'zones': serializer.data,
        # 'strengths':serializer2.data
    })


@api_view(['GET'])
def search_data(request):
    zip_code = request.GET['zip']
    try:
        latitude = ZipCodes.objects.get(zip_code=zip_code).latitude
        zone_data = Zones.objects.filter(LatitudeMin__lte=latitude, LatitudeMax__gte=latitude)
        serializer = ZoneSerializer(zone_data, many=True, context={'request': request})
        if not serializer.is_valid():
            return Response({
                'status': True,
                'message': 'some errors occured!',
                'data': serializer.errors
            })

    except Exception as e:
        print(e)
    return Response({
        'status': True,
        'message': "Fetched Successfully!!",
        'data': serializer.data
    })
