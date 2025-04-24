from rest_framework import viewsets
from accounts.models import Account, Deposit
from accounts.serializers import AccountSerializer, DepositSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer


class DepositViewSet(viewsets.ModelViewSet):
    queryset=Deposit.objects.all()
    serializer_class=DepositSerializer