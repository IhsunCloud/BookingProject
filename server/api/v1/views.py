from api.v1.subviews.booking.views import BookingViewSet
from api.v1.subviews.user.views import RegisterViewSet



# TODO: This should be moved to sub_views directory.
from rest_framework import viewsets

from agency.models import Agency
from airport.models import Airport
from bus.models import BusReservation
from home.models import Home
from hotel.models import Hotel

from . import serializers


class AgencyViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.AgencySerializer
	queryset = Agency.objects.all()


class AirportViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.AirportSerializer
	queryset = Airport.objects.all()


class BusReservationViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.BusSerializer
	queryset = BusReservation.objects.all()


class HomeViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.HomeSerializer
	queryset = Home.objects.all()


class HotelViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.HotelSerializer
	queryset = Hotel.objects.all()
