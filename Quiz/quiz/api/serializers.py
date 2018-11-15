from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Advert


class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'is_staff']


class AdvertModelSerialier(serializers.ModelSerializer):
    owner = UserModelSerializer(read_only=True)

    class Meta:
        model = Advert
        fields = ['id', 'title', 'address', 'description', 'price', 'number_of_views', 'owner']
