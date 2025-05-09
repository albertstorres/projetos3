from customers.models import Customer
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class CustomerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only = True)
    password = serializers.CharField(write_only = True)
    
    
    class Meta:
        model = Customer
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
    
    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')

        user = User.objects.create_user(
            username=username,
            password=password
        )

        try:
            clientes_group = Group.objects.get(name = 'Clientes')
            user.groups.add(clientes_group)
        except Group.DoesNotExist:
            raise serializers.ValidationError("Grupo não encontrado.")
        
        customer = Customer.objects.create(user = user, **validated_data)

        return customer