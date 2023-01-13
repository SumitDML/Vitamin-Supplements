import enum

from django.shortcuts import render
from django.db import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app.util import switch, switcher
from rest_framework.pagination import  LimitOffsetPagination
from rest_framework.generics import ListAPIView


@api_view(['GET'])
def get_tabs(request):
    tabId = request.GET.get('tabId')
    page_number = request.GET.get('page')
    try:
        if tabId is None:
            parents = Tabs.objects.all()
            # p = Paginator(parents, 1)
            # if not parents.exists():
            #     return Response({
            #         'status': False,
            #         'message': "No Records Found!",
            #     })
            # try:
            #     page_obj = p.get_page(page_number)
            # except PageNotAnInteger:
            #     page_obj = p.page(1)
            serializer = TabSerializer(parents, many=True)

            return Response({
                'status': 200,
                'message': "Data Fetched Successfully!",
                'data': serializer.data,

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
    tabId = request.GET.get('tab_id')
    all_childs = TabChild.objects.filter(tab_id=tabId)
    if not all_childs.exists():
        return Response({
            'status': False,
            'message': "No Childs Found!",
        })

    serializer = TabChildSerializer(all_childs, many=True, context={'request': request})
    return Response({
        'status': True,
        'message': "Fetched Successfully!!",
        'data': serializer.data
    })


@api_view(['GET'])
def get_child_data(request):
    tabId = request.GET.get('tab_id')
    tabChildId = request.GET.get('tab_child_id')
    page_number = request.GET.get('page')

    try:
        all_childs = TabChild.objects.filter(tab_id=tabId)

        if not all_childs.exists():
            return Response({
                'status': False,
                'message': "No Child Record Found!",
            })
        result = all_childs.filter(tab_child_id=tabChildId)
        if not result.exists():
            return Response({
                'status': False,
                'message': "Invali child Id!",
            })

        serializer = TabChildnameSerializer(result, many=True, context={'request': request})
        name = serializer.data[0].get('name')
        model = switch(name)
        serializer1 = getGenericSerializer(model)
        data = model.objects.all().order_by('id')
        p = Paginator(data, 25)
        try:
            page_obj = p.get_page(page_number)  # returns the desired page object
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = p.page(1)
        except EmptyPage:
            # get the lat page data if the page_number is bigger than last page number.
            page_obj = p.page(p.num_pages)
        serialized_data = serializer1(page_obj, many=True, context={'request': request})
        totalPage=p.page_range.stop-1

        return Response({
            'status': True,
            'message': "Fetched Successfully!!",
            'tab_id': tabId,
            'page_size':totalPage,
            'data': serialized_data.data

        })
    except Exception as e:
        print(e)
    return Response({
        'status': True,
        'message': "Sorry ! Some Error Occured!",
    })

#
# @api_view(['GET'])
# def search_data(request):
#         zip_code = request.GET['zip']
#         latitude = ZipCodes.objects.get(zip_code=zip_code).latitude
#         if not latitude is None:
#             return Response({
#                 'status': False,
#                 'message': "Invalid Zip-Code",
#             })
#         zone_data = Zones.objects.filter(LatitudeMin__lte=latitude, LatitudeMax__gte=latitude)
#         serializer = ZoneViewSerializer(zone_data, many=True, context={'request': request})
#
#         return Response({
#             'status': True,
#             'message': "Fetched Successfully!!",
#             'data': serializer.data
#         })
#
# @api_view(['GET'])
# def view_data(request):
#     vitamin = request.GET['keyword']
#     try:
#
#         zones = Zones.objects.filter(vitamin_type=vitamin)
#         strength = SunshineAvailability.objects.filter(vitamin_type=vitamin)
#         serializer = ZoneViewSerializer(zones, many=True, context={'request': request})
#         serializer2 = SunshineAvailabilitySerializer(strength, many=True, context={'request': request})
#         return Response({
#             'status': True,
#             'message': "Fetched Successfully!!",
#             'zones': serializer.data,
#             'strengths': serializer2.data
#         })
#     except Exception as e:
#         print(e)
#     return Response({
#         'status': True,
#         'message': "Error Occured!",
#         # 'zones': serializer.data,
#         # 'strengths':serializer2.data
#     })


@api_view(['GET'])
def result_data(request):
    # data = []
    zip_code = request.GET['zip']

    try:
        latitude = ZipCodes.objects.get(zip_code=zip_code).latitude
        zone_data = Zones.objects.filter(LatitudeMin__lte=latitude, LatitudeMax__gte=latitude)
        serializer = ZoneViewSerializer(zone_data, many=True, context={'request': request})
        # result = serializer.data
        # for itr in result:
        #     raw = SunshineAvailability.objects.filter(ZoneID=itr['ZoneID'])
        #     serializer1 = SunshineAvailabilitySerializer(raw, many=True, context={'request': request})
        #     data.append(serializer1.data)

    except ZipCodes.DoesNotExist:
        return Response({
            'status': False,
            'message': "Invalid Zip-Code!",
        })
    except Exception as e:
        return Response({
            'status': False,
            'message': "Something went wrong!",
        })
    return Response({
        'status': True,
        'message': "Fetched Successfully!!",
        'zones': serializer.data,
    })
