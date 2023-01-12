from django.urls import path
from .views import *

urlpatterns = [

    path('search/', search_data, name="search_data"),
    path('tabs/listing/', get_tabs, name="get_tabs"),
    path('tabs/child/listing', get_tab_childs, name="get_tab_childs"),
    path('tabs/child/data', get_child_data, name="get_child_data"),


]
