from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *


# Create your views here.


@api_view(['GET'])
def view_data(request):
    zip_code = request.GET['zip']
    try:
        # data = SunshineAvailability.objects.all()
        # serializer = SunshineAvailabilitySerializer(data=data, many=True, context={'request': request})
        # if serializer.is_valid():
        #     return Response({
        #                 'status': True,
        #                 'message': "Fetched Successfully!!",
        #                 'zones': serializer.data
        #         })
        data = []
        latitude = ZipCodes.objects.get(zip_code=zip_code).latitude
        zone_data = Zones.objects.filter(LatitudeMin__lte=latitude, LatitudeMax__gte=latitude)
        serializer = ZoneSerializer(data=zone_data, many=True, context={'request': request})
        if serializer.is_valid():

            for i in zone_data:
                zone_data
                SunshineAvailability.objects.filter(ZoneId=zoneId).value_list(flat=True)
                data.append()

                return Response({
                        'status': True,
                        'message': "Fetched Successfully!!",
                        'data': data
                })
    except Exception as e:
        print(e)

    return Response({
        'status': True,
        'message': "Fetched Successfully!!",
        'data': data
    })
