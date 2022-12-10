from rest_framework.generics import ModelViewSet

from booking import models


class BookingViewSet(ModelViewSet):
    serializer_class = models.Booking
    