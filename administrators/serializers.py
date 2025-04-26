from administrators.models import Administrator
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class AdministratorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)


    class Meta:
        model=Administrator
        fields=['username', 'password', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')

        user = User.objects.create_user(
            username = username,
            password = password,
            is_staff = True
        )

        try:
            administradores_group = Group.objects.get(name='Administradores')
            user.groups.add(administradores_group)
        except Group.DoesNotExist:
            raise serializers.ValidationError("Grupo não encontrado.")

        administrator = Administrator.objects.create(user=user, **validated_data)

        return administrator