from enum import IntEnum

from django.db import models

vitamin_types = (
    (1, "Vitamin_A"),
    (2, "Vitamin_B"),
    (3, "Vitamin_C"),
    (4, "Vitamin_D"),
)


class Zones(models.Model):
    ZoneID = models.IntegerField(primary_key=True, editable=False, name='ZoneID')
    LatitudeMin = models.FloatField(name='LatitudeMin')
    LatitudeMax = models.FloatField(name='LatitudeMax')
    NorthSouth = models.CharField(max_length=1, name='NorthSouth')
    vitamin_type = models.IntegerField(choices=vitamin_types,default=1)

    class Meta:
        db_table = 'Zones'


class SunshineAvailability(models.Model):
    sunshine_id = models.AutoField(primary_key=True, editable=False, name='SunshineId', null=False)
    Month = models.IntegerField(name='Month')
    Strength = models.IntegerField(name='Strength')
    vitamin_type = models.IntegerField(choices=vitamin_types, default=1,null=True)
    ZoneID = models.ForeignKey(name='ZoneID')

    class Meta:
        db_table = 'Sunshine_Availability'


class ZipCodes(models.Model):
    zipCode = models.CharField(max_length=5, name='zip_code', primary_key=True, editable=False, null=False)
    latitude = models.FloatField(name='latitude', null=False)
    longitude = models.FloatField(name='longitude', null=False)

    class Meta:
        db_table = 'zip_codes'
