from django.db import models


# Create your models here.

class Zones(models.Model):
    ZoneID = models.IntegerField(primary_key=True, editable=False)
    LatitudeMin = models.FloatField()
    LatitudeMax = models.FloatField()
    NorthSouth = models.CharField(max_length=1)


class VitaminStrength(models.Model):
    Month = models.IntegerField()
    Strength = models.IntegerField()
    Zone = models.ForeignKey(Zones, on_delete=models.CASCADE)
