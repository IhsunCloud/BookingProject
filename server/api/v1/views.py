from api.v1.subviews.booking.views import BookingViewSet
from api.v1.subviews.user.views import RegisterViewSet





# TODO: This should be moved to sub_views directory.
from datetime import datetime

from django.utils import timezone

from rest_framework import filters
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
	serializer_class = serializers.BusReservationSerializer
	queryset = BusReservation.objects.filter(
		time_to_go__gt=timezone.now(), is_reserved=False).all()

	search_fields = [
		'address',
		'time_to_go',
		'seat_number'
	]

	def perform_create(self, serializer):
		"""
		The request user is set as author automatically.
		"""
		serializer.save(user=self.request.user)


class HomeViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.HomeSerializer
	queryset  = Home.objects.filter(
		entry_at__gte= timezone.now(), is_reserved=False).all()    
	filter_backends  = (filters.SearchFilter,)

	search_fields = [
		'address',
		'name',
		'home_class',
		'entry_at',
		'is_premium',
		'is_reserved',
		'price'
	]

	def perform_create(self, serializer):
		"""
		The request user is set as author automatically.
		"""
		serializer.save(user=self.request.user)


class HotelViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.HotelSerializer
	queryset = Hotel.objects.filter(
		entry_at__gte= timezone.now(), is_reserved=False).all()
    
	filter_backends  = (filters.SearchFilter,)

	search_fields = [
		'address',
		'name',
		'hotel_class'
	]

	def perform_create(self, serializer):
		"""
		The request user is set as author automatically.
		"""
		serializer.save(user=self.request.user)
