from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  destination = models.CharField(max_length=200)
  departure_date = models.DateField(null=True)
  return_date = models.DateField(null=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.destination

  class Meta:
    ordering = ['departure_date']
  

class LuggageItem(models.Model):
  trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
  item = models.CharField(max_length=200)
  quantity = models.IntegerField(validators=[MinValueValidator(1)])
  departure_checked = models.BooleanField(default=False)
  return_checked = models.BooleanField(default=False)

  def __str__(self):
      return self.item
  