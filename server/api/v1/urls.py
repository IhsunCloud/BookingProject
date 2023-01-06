from django.urls import path, include

from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

from api.v1 import views as api_views_v1


router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('token/', jwt_views.TokenObtainPairView.as_view()),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view()),

    path('agency/', api_views_v1.AgencyViewSet.as_view(
        {'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),

    path('airport/', api_views_v1.AirportViewSet.as_view(
        {'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),

    path('booking/', api_views_v1.BookingViewSet.as_view(
        {'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),

    path('bus-reservation/', api_views_v1.BusReservationViewSet.as_view(
        {'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),

    path('home/', api_views_v1.HomeViewSet.as_view(
        {'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),

    path('hotel/', api_views_v1.HotelViewSet.as_view(
        {'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),

    path('register/', api_views_v1.RegisterViewSet.as_view(
        {'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'}))
    ]

