from rest_framework.permissions import DjangoModelPermissions
from rest_framework import viewsets
from orders.models import Order, OrderProducts
from orders.serializers import OrderSerializer, OrderProductsSerializer
from core.permissions import IsAccountOwner
from customers.models import Customer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [DjangoModelPermissions, IsAccountOwner]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Order.objects.all()
        
        try:
            customer = Customer.objects.get(user = user)
            return Order.objects.filter(customer_id=customer)
        except Customer.DoesNotExist:
            return Order.objects.none()


class OrderProductsViewSet(viewsets.ModelViewSet):
    queryset = OrderProducts.objects.all()
    serializer_class = OrderProductsSerializer
    permission_classes = [DjangoModelPermissions]