from rest_framework import serializers
from administrators.models import Administrator


class AdministratorSerializer(serializers.ModelSerializer):


    class Meta:
        model=Administrator
        fields='__all__'