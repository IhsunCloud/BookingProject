from django.contrib import admin
from cart import models

admin.site.register(models.Order)
admin.site.register(models.OrderItem)