"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from luggage import views
from rest_framework import routers

# Declaration of the `router` object
router = routers.DefaultRouter()

# The `register` method we will use with the `router` object has two mandatory arguments:
# 1. `prefix`: the URL prefix we will use for this set of routes (preceded by an 'r')
# 2. `viewset`: the viewset class
# We will also use the optional `basename` argument to set a base for the URLs that will be created.
router.register(r'trips', views.TripView, 'trip')
router.register(r'items', views.LuggageItemView, 'item-list')

# The new 'api' route will take us to the "Django REST framework" website,
# where we will be able to view our model instances as JSON objects.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
