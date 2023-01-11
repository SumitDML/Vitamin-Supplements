from django.urls import path
from .views import view_data

urlpatterns = [

    path('get/', view_data, name="view_data"),

]
