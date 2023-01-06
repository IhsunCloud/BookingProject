from django.contrib import admin
from bus import models


admin.site.register(models.Adult)
admin.site.register(models.Bus)
admin.site.register(models.BusReservation)
admin.site.register(models.Passenger)
admin.site.register(models.Underage)
