from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.apartments.models import Apartment


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ['name', 'slug', 'description', 'price', 'number_of_rooms', 'square', 'availability', 'owner', 'created_at', 'updated_at']

