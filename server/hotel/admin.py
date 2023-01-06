from django.contrib import admin
from hotel import models


admin.site.register(models.Adult)
admin.site.register(models.Underage)
admin.site.register(models.Hotel)
admin.site.register(models.Image)
admin.site.register(models.Passenger)
admin.site.register(models.Phone)
admin.site.register(models.Reviews)
admin.site.register(models.Room)