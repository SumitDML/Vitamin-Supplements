# Generated by Django 4.1.5 on 2023-01-11 11:31

from django.db import migrations


class Migration(migrations.Migration):
    def initiateData(self, schema_editor):

        from django.conf import settings
        from sqlalchemy import create_engine
        import pandas as pd
        from app.models import SunshineAvailability,Zones

        xls = pd.ExcelFile('app/data/Vitamin D (1).xlsx')
        df1 = pd.read_excel(xls, 'Vitamin D Strength')
        df2 = pd.read_excel(xls, 'Zones')
        df1.columns = ["zone_id", "Month", "Strength"]
        df2.columns = ["ZoneID", "LatitudeMin", "LatitudeMax", "NorthSouth"]
        df2.set_index("ZoneID", inplace=True)


        for df1 in df1.itertuples():
            obj = SunshineAvailability.objects.create(month=df1.Month, strength=df1.Strength,zone=df1.zone_id)
            obj.save()

        for df2 in df2.itertuples():
            obj1 = Zones.objects.create(zoneID=df2.ZoneID, latitudeMin=df2.LatitudeMin,latitudeMax=df2.LatitudeMax, northSouth=df2.NorthSouth)
            obj1.save()

    dependencies = [
        ('app', '0002_auto_20230111_1131'),
    ]

    operations = [
        migrations.RunPython(initiateData)
    ]
