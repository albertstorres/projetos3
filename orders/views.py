from rest_framework.permissions import DjangoModelPermissions
from rest_framework import viewsets
from orders.models import Order, OrderProducts
from orders.serializers import OrderSerializer, OrderProductsSerializer
from core.permissions import IsAccountOwner


class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    permission_classes=[DjangoModelPermissions, IsAccountOwner]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Order.objects.all()
        
        return Order.objects.filter(account_id__user=user)


class OrderProductsViewSet(viewsets.ModelViewSet):
    queryset=OrderProducts.objects.all()
    serializer_class=OrderProductsSerializer
    permission_classes=[DjangoModelPermissions]