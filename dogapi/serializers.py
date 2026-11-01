from rest_framework import serializers
from .models import Dog, Breed

#handles Breed data
class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'

#handes Dog data, including the foreign key to Breed
class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'

