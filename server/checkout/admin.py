from django.contrib import admin
from checkout import models


admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.PriceBooking)
admin.site.register(models.Currency)
admin.site.register(models.Price)
admin.site.register(models.CurrencyExchangeRate)