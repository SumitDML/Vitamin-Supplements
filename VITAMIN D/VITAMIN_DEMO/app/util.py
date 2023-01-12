
from .models import *
def switch(name):
    return switcher.get(name, default)()
def zones():
    return Zones
def Sunshine_availibilty():
    return SunshineAvailability
def default():
    return "Invalid Model"

switcher = {
    "Zones": zones,
    "Sunshine_Availability": Sunshine_availibilty
}
