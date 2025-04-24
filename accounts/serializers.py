from rest_framework import serializers
from accounts.models import Account, Deposit


class AccountSerializer(serializers.ModelSerializer):


    class Meta:
        model=Account
        fields='__all__'


class DepositSerializer(serializers.ModelSerializer):


    class Meta:
        model=Deposit
        fields='__all__'