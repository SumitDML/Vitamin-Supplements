from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *


# Create your views here.


@api_view(['GET'])
def view_data(request):
        zip_code = request.GET['zip']
        try:
            latitude = ZipCodes.objects.get(zip_code=zip_code).latitude
            zone_data = Zones.objects.filter(LatitudeMin__lte=latitude, LatitudeMax__gte=latitude)
            print(zone_data)
            serializer = ZoneSerializer(data=zone_data, many=True, context={'request': request})

            result = SunshineAvailability.objects.filter(zoneId=4).value_list(flat=True)
            print(result)
            serializer = SunshineAvailabilitySerializer(data=result, many=True, context={'request': request})
            if serializer.is_valid():
                return Response({
                    'status': True,
                    'message': "Fetched Successfully!!",
                    'data': serializer.data
                 })
        except Exception as e:
            print(e)

        return Response({
        'status': True,
        'message': "Fetched Successfully!!",

    })


