from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    #
    # def ready(self):
    #     import pandas as pd
    #     from tablib import Dataset
    #     # from .resources import ZonesResources, SunshineAvailabilityResources
    #     from .models import Zones, SunshineAvailability
    #
    #     xls = pd.ExcelFile('app/data/Vitamin D (1).xlsx')
    #     sunshine_availability_data = pd.read_excel(xls, 'Vitamin D Strength')
    #     zones_data = pd.read_excel(xls, 'Zones')
    #
    #     sunshine_availability_data.columns = ["ZoneID", "Month", "Strength"]
    #     zones_data.columns = ["ZoneID", "LatitudeMin", "LatitudeMax", "NorthSouth"]
    #
    #     zones_data.set_index("ZoneID", inplace=True)
    #     dataset = Dataset()
    #     imported_data = dataset.load(zones_data)
    #     imported_data2 = dataset.load(sunshine_availability_data)
    #
    #     for data in imported_data:
    #         value = Zones(
    #             data[0],
    #             data[1],
    #             data[2]
    #         )
    #         value.save()
    #
    #     for data2 in imported_data2:
    #         value2 = SunshineAvailability(
    #             data2[0],
    #             data2[1],
    #             data2[2]
    #         )
    #         value2.save()
