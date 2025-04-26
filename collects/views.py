from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework import viewsets
from collects.models import Address, Categorie, Collect
from collects.serializers import AddressSerializer, CategorieSerializer, CollectSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [DjangoModelPermissions]


class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser]


class CollectViewSet(viewsets.ModelViewSet):
    queryset = Collect.objects.all()
    serializer_class = CollectSerializer
    permission_classes = [DjangoModelPermissions]