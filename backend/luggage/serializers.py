from rest_framework import serializers
from .models import User, Trip, LuggageItem

# This REST serializer converts our model classes to JSON for the client
# and helps make CRUD requests with a JSON payload to the API.

class LuggageItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = LuggageItem
    fields = ['item', 'quantity', 'departure_checked', 'return_checked']

class TripSerializer(serializers.ModelSerializer):
  # The following serializers are related to the fields from the Django User model. 
  username = serializers.CharField(source='user.username')
  email = serializers.CharField(source='user.email')
  password = serializers.CharField(source='user.password', write_only=True)

  # The following serializer represents a nested relationship.
  luggage_items = LuggageItemSerializer(many=True, read_only=True)

  class Meta:
    model = Trip
    fields = ('username', 'email', 'password', 'destination', 'departure_date', 'return_date', 'created', 'luggage_items')



