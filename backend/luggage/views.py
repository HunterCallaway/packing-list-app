from django.shortcuts import render

from rest_framework import viewsets
from .serializers import LuggageItemSerializer, TripSerializer
from .models import LuggageItem, Trip

# `ModelViewSet` inherits from `GenericAPIView`. It requires us to set the `serializer_class`
# and `queryset` attributes.
# The `serializer_class` attribute allows us to specify the serializer class to use for
# validating and deserializing input and serializing output.
# Setting the `queryset` attribute to `[Model].objects.all()` 
# allows us populate everything from the model we are using.

class LuggageItemView(viewsets.ModelViewSet):
  serializer_class = LuggageItemSerializer
  queryset = LuggageItem.objects.all()

class TripView(viewsets.ModelViewSet):
  serializer_class = LuggageItemSerializer
  queryset = Trip.objects.all()
  
