from django.db import models


class RoomTypes(models.TextChoices):
    MOUNTAIN_VIEW    = 'MV', ('Mountain view')
    CITY_VIEW        = 'CT', ('City view')
    LANDMARK_VIEW    = 'LM', ('Landmark view')
    BRIDAL_SUITE     = 'BS', ('Bridal suite')
    NON_SMOKING_ROOM = 'NS',('Non-smoking rooms')
    SUITS            = 'ST' ,('Suites')
    FAMILY_ROOM      = 'FR' ,('Family rooms')
    SMOKING_ROOMS_AVAILABLE = 'SR' ,('Smoking rooms available')


class RoomFeatures(models.TextChoices):
    ALLERGY_FREE_ROOM   = 'AF', ('Allergy-free room')
    BLACKOUT_CURTAINS   = 'BC', ('Blackout curtains')
    AIR_CONDITIONING    = 'AC', ('Air conditioning')
    ADDITIONAL_BATHROOM = 'AB', ('Additional bathroom')
    COFFEE_TEA_MAKER    = 'CT', ('Coffee / tea maker')
    CABLE_SATELLITE_TV  = 'CS', ('Cable / satellite TV')
    BIDET = 'BD', ('Bidet')
    DESK  = 'DS', ('Desk')


class PropertyAmenities(models.TextChoices):
    AIRPORT_TRANSPORTATION = 'AT', ('Airport transportation')
    FREE_BREKFEAST         = 'FB', ('Free breakfast')
    FITNESS_CENTER         = 'FC', ('Fitness Center with Gym / Workout Room')
    FREE_HIGH_SPEED_WIFI   = 'FI', ('Free High Speed Internet (WiFi)')
    FREE_PARKING           = 'FP', ('Free parking')
    HIGHCHAR_AVAILABLE     = 'HA', ('Highchairs available')
    KIDS_STAY_FREE         = 'KS', ('Kids stay free')
    POOL                   = 'PL', ('Pool')