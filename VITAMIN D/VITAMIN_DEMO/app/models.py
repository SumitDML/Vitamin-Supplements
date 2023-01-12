from enum import IntEnum

from django.db import models

vitamin_types = (
    (1, "Vitamin_A"),
    (2, "Vitamin_B"),
    (3, "Vitamin_C"),
    (4, "Vitamin_D"),
)


class Tabs(models.Model):
    tabId = models.AutoField(primary_key=True, editable=False, name='tab_id')
    name = models.CharField(name='name', max_length=255)
    displayName = models.CharField(name='display_name', max_length=255)
    createdAt = models.DateTimeField(auto_now=True, name='created_at', null=True)
    updatedAt = models.DateTimeField(auto_now_add=True, name='updated_at', null=True)

    class Meta:
        db_table = 'tabs'

    def __str__(self):
        return self.name


class TabChild(models.Model):
    tabChildId = models.AutoField(primary_key=True, editable=False, name='tab_child_id')
    name = models.CharField(name='name', max_length=255)
    displayName = models.CharField(name='display_name', max_length=255)
    tabs = models.ForeignKey(Tabs, on_delete=models.CASCADE, related_name='childs', name='tab', null=True)
    createdAt = models.DateTimeField(auto_now=True, name='created_at', null=True)
    updatedAt = models.DateTimeField(auto_now_add=True, name='updated_at', null=True)

    class Meta:
        db_table = 'tab_childs'

    def __str__(self):
        return self.name


class TabChildMappings(models.Model):
    tabId = models.ForeignKey(Tabs, on_delete=models.CASCADE, related_name='tabs', name='tab', null=True)
    tabChildId = models.ForeignKey(TabChild, on_delete=models.CASCADE, related_name='childs', name='tab_child',null=True)

    class Meta:
        db_table = 'tab_child_mappings'

    def __str__(self):
        return self.name


class Zones(models.Model):
    ZoneID = models.IntegerField(primary_key=True, editable=False, name='ZoneID')
    LatitudeMin = models.FloatField(name='LatitudeMin')
    LatitudeMax = models.FloatField(name='LatitudeMax')
    NorthSouth = models.CharField(max_length=1, name='NorthSouth')

    class Meta:
        db_table = 'zones'

    def __str__(self):
        return self.name


class SunshineAvailability(models.Model):
    sunshine_id = models.AutoField(primary_key=True, editable=False, name='SunshineId', null=False)
    Month = models.IntegerField(name='Month')
    Strength = models.IntegerField(name='Strength')
    ZoneID = models.ForeignKey('Zones', on_delete=models.CASCADE, related_name='strengths', name='ZoneID', null=True)

    class Meta:
        db_table = 'sunshine_availibilty'

    def __str__(self):
        return self.name


class ZipCodes(models.Model):
    zipCode = models.CharField(max_length=5, name='zip_code', primary_key=True, editable=False, null=False)
    latitude = models.FloatField(name='latitude', null=False)
    longitude = models.FloatField(name='longitude', null=False)

    class Meta:
        db_table = 'zip_codes'

    def __str__(self):
        return self.name
