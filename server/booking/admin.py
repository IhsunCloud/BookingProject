from django.contrib import admin
from booking import models


admin.site.register(models.Booking)
admin.site.register(models.BookingError)
admin.site.register(models.BookingItem)
admin.site.register(models.ExtraPersonInfo)
