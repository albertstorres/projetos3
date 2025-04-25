from rest_framework.permissions import DjangoModelPermissions
from rest_framework import viewsets
from accounts.models import Account, Deposit
from accounts.serializers import AccountSerializer, DepositSerializer
from core.permissions import IsAccountOwner


class AccountViewSet(viewsets.ModelViewSet):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer
    permission_classes=DjangoModelPermissions


class DepositViewSet(viewsets.ModelViewSet):
    queryset=Deposit.objects.all()
    serializer_class=[DepositSerializer, IsAccountOwner]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Deposit.objects.all()
        
        return Deposit.objects.filter(account_id__user=user)