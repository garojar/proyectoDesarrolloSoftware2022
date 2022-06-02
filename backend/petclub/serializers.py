from rest_framework import serializers
from petclub.models import (
    Pet,
    Person,
)


class CustomPetSerializer(serializers.Serializer):

    name = serializers.CharField()
    species = serializers.CharField()

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'

class PersonCustomSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    rut = serializers.CharField(required=True)
    age = serializers.IntegerField(required=False)


class PetModelSerializer(serializers.ModelSerializer):

    owner = PersonSerializer()

    class Meta:
        model = Pet
        exclude = [
            'weight',
        ]
