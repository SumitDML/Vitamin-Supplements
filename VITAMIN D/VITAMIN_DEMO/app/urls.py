from django.urls import path
from .views import search_data,view_data

urlpatterns = [

    path('search/', search_data, name="search_data"),
    path('view/',   view_data, name="view_data"),


]
