from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework import viewsets
from core.permissions import IsAccountOwner
from collects.models import Address, Categorie, Collect
from collects.serializers import AddressSerializer, CategorieSerializer, CollectSerializer
from collects.filters import AddressFilterClass, CategorieFilterClass, CollectFilterClass


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [DjangoModelPermissions, IsAccountOwner]
    rql_filter_class = AddressFilterClass

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Address.objects.all()

        return Address.objects.filter(customer_id__user = user)


class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser] #REVISAR! cliente não deve conseguir fazer um GET
    rql_filter_class = CategorieFilterClass


class CollectViewSet(viewsets.ModelViewSet):
    queryset = Collect.objects.all()
    serializer_class = CollectSerializer
    permission_classes = [DjangoModelPermissions, IsAccountOwner]
    rql_filter_class = CollectFilterClass

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Collect.objects.all()
        
        return Collect.objects.filter(customer_id__user = user)