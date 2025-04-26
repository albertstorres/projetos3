from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework import viewsets
from products.models import Product
from products.serializers import ProductSerializer
from products.filters import ProductFilterClass


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissions]
    rql_filter_class = ProductFilterClass