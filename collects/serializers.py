from rest_framework import serializers
from collects.models import Address, Categorie, Collect


class AddressSerializer(serializers.ModelSerializer):


    class Meta:
        model=Address
        fields='__all__'


class CategorieSerializer(serializers.ModelSerializer):


    class Meta:
        model=Categorie
        fields='__all__'


class CollectSerializer(serializers.ModelSerializer):


    class Meta:
        model=Collect
        fields='__all__'