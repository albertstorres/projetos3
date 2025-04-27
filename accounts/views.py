from rest_framework.permissions import DjangoModelPermissions
from rest_framework import viewsets
from accounts.models import Account, Deposit
from accounts.serializers import AccountSerializer, DepositSerializer
from core.permissions import IsAccountOwner
from accounts.filters import AccountFilterClass, DepositFilterClass
from customers.models import Customer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [DjangoModelPermissions, IsAccountOwner]
    rql_filter_class = AccountFilterClass


class DepositViewSet(viewsets.ModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer
    permission_classes = [IsAccountOwner]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Deposit.objects.all()
        
        customer = Customer.objects.filter(user=user).first()
        if not customer:
            return Deposit.objects.none()

        account_customer = Account.objects.filter(customer_id=customer)
        if not account_customer:
            return Deposit.objects.none()
        
        return Deposit.objects.filter(account_id=account_customer)