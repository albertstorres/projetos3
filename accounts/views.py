from rest_framework.permissions import DjangoModelPermissions
from rest_framework import viewsets
from accounts.models import Account, Deposit
from accounts.serializers import AccountSerializer, DepositSerializer
from core.permissions import IsAccountOwner
from accounts.filters import AccountFilterClass, DepositFilterClass
from customers.models import Customer
from rest_framework.views import APIView
from rest_framework.response import Response

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
        
        return Deposit.objects.filter(account_id__in=account_customer)

class GetBalanceView(APIView):
    permission_classes = [IsAccountOwner]

    def get(self, request):
        user = request.user

        if user.is_staff:
            return Response({"detail": "Staff users don't have personal account balances."}, status=400)

        customer = Customer.objects.filter(user=user).first()
        if not customer:
            return Response({"balance": 0.00})

        account = Account.objects.filter(customer_id=customer).first()
        if not account:
            return Response({"balance": 0.00})

        return Response({"balance": account.balance})