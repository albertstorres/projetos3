from rest_framework import viewsets
from customers.models import Customer
from customers.serializers import CustomerSerializer
from customers.filters import CustomerFilterClass


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    rql_filter_class = CustomerFilterClass