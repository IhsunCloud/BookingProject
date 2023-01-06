from django_otp.admin import OTPAdminSite
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


# Secure Django Admin
# admin.site.__class__ = OTPAdminSite
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.v1.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)