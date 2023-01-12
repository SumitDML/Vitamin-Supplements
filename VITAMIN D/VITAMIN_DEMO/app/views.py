import enum

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


@api_view(['GET'])
def get_tabs(request):
    tabId = request.GET.get('tabId')
    try:

        if tabId is None:
            parents = Tabs.objects.all()
            if not parents.exists():
                return Response({
                    'status': False,
                    'message': "No Records Found!",
                })
            serializer = TabSerializer(parents, many=True)
            return Response({
                'status': 200,
                'message': "Data Fetched Successfully!",
                'data': serializer.data
            })

        else:
            parents = Tabs.objects.filter(tab_id=tabId)
            if not parents.exists():
                return Response({
                    'status': False,
                    'message': "No Records Found!",
                })
            serializers1 = TabSerializer(parents, many=True)
            return Response({
                'status': 200,
                'message': "Data Fetched Successfully!",
                'data': serializers1.data
            })
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': "Some Error Occured!",
    })


@api_view(['GET'])
def get_tab_childs(request):
    tabChildId = request.GET.get('tab_child_id')
    if tabChildId is None:
        childs = TabChild.objects.all()
        if not childs.exists():
            return Response({
                'status': False,
                'message': "No Records Found!",
            })
        serializer1 = TabChildSerializer(childs, many=True)
        return Response({
            'status': True,
            'message': "Data Fetched Successfully!",
            'data': serializer1.data
        })

    else:
        childs = TabChild.objects.filter(tab_child_id=tabChildId)
        serializers = TabChildSerializer(childs, many=True)
        return Response({
            'status': True,
            'message': "Data Fetched Successfully!",
            'data': serializers.data
        })



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


@api_view(['GET'])
def result_data(request):
    data = []
    zip_code = request.GET['zip']
    try:
        latitude = ZipCodes.objects.get(zip_code=zip_code).latitude
        zone_data = Zones.objects.filter(LatitudeMin__lte=latitude, LatitudeMax__gte=latitude)
        serializer = ZoneViewSerializer(zone_data, many=True, context={'request': request})
        result = serializer.data
        for itr in result:
            raw = SunshineAvailability.objects.filter(ZoneID=itr['ZoneID'])
            serializer1 = SunshineAvailabilitySerializer(raw, many=True, context={'request': request})
            data.append(serializer1.data)

    except Exception as e:
        print(e)
    return Response({
        'status': True,
        'message': "Fetched Successfully!!",
        'zones': serializer.data,
        'strengths': data
    })
