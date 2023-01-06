from rest_framework import viewsets
from agency.models import Agency

from api.v1.serializers import AgencySerializer


class AgencyViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for CRUD Agency.
    """
    serializer_class = AgencySerializer
    query_set = Agency.objects.all()