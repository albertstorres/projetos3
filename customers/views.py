from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from customers.models import Customer
from customers.serializers import CustomerSerializer
from customers.filters import CustomerFilterClass


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    rql_filter_class = CustomerFilterClass

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Customer.objects.all()

        return Customer.objects.filter(user=user)
    
    def patch(self, request, *args, **kwargs):
        user = self.request.user

        customer = Customer.objects.filter(user = user).first()
        if customer.user != user and not user.is_staff:
            raise PermissionDenied('Você não tem permissão para atualizar este cliente.')
        
        return super().update(request, *args, **kwargs)