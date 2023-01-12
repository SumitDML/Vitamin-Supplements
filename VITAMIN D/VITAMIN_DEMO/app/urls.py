from django.urls import path
from .views import *

urlpatterns = [

    path('search/', search_data, name="search_data"),
    path('view/',   view_data, name="view_data"),
    path('view_result/', result_data, name="result_data"),
    path('getTabs/', get_tabs, name="get_tabs"),
    path('getChilds/', get_tab_childs, name="get_tab_childs"),


]
