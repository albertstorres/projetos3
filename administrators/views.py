from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework import viewsets
from administrators.models import Administrator
from administrators.serializers import AdministratorSerializer
from administrators.filters import AdministratorFielterClass


class AdministratorViewSet(viewsets.ModelViewSet):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    rql_filter_class = AdministratorFielterClass