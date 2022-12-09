from django.urls import path, include

from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

from api.v1 import views as api_views_v1


router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('register/', api_views_v1.RegisterAPIView.as_view()),
    path('token/', jwt_views.TokenObtainPairView.as_view()),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view()),
]