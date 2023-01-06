from datetime import datetime

from rest_framework import filters
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import viewsets

from booking.models import Booking
from api.v1.serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for CRUD Bookings.
    """
    serializer_class = BookingSerializer
    filter_backends  = (filters.SearchFilter,)

    queryset = Booking.objects.filter(
        date_from__gt = datetime.now()).all()

    search_fields = [
        'date_from',
        'date_until',
        'time_period',
        'time_unit'
    ]

    def perform_create(self, serializer):
        """
        The request user is set as author automatically.
        """
        serializer.save(user=self.request.user)
