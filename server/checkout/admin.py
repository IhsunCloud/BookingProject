from django.contrib import admin
from checkout import models

admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.PriceBooking)