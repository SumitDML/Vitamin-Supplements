from django.db import models


class Zones(models.Model):
    zoneID = models.IntegerField(primary_key=True, editable=False, name='ZoneID')
    latitudeMin = models.FloatField(name='LatitudeMin')
    latitudeMax = models.FloatField(name='LatitudeMax')
    northSouth = models.CharField(max_length=1, name='NorthSouth')

    class Meta:
        db_table = 'Zones'


class SunshineAvailability(models.Model):
    id = models.AutoField(primary_key=True)
    month = models.IntegerField(name='Month')
    strength = models.IntegerField(name=' Strength')
    zone = models.ForeignKey(Zones, on_delete=models.CASCADE, name='ZoneId')

    class Meta:
        db_table = 'Sunshine_Availability'


class ZipCodes(models.Model):
    zipCode = models.CharField(max_length=5, name='zip_code', primary_key=True, editable=False, null=False)
    latitude = models.FloatField(name='latitude', null=False)
    longitude = models.FloatField(name='longitude', null=False)

    class Meta:
        db_table = 'zip_codes'
