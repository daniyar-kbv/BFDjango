from rest_framework import serializers
from main.models import List
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=300)
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()


class ListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    created_by = UserSerializer(read_only=True)

    def create(self, validated_data):
        list = List(**validated_data)
        list.created_by = User.objects.filter.first()
        list.save()
        return list

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class ListModelSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = List
        fields = ['id', 'name', 'created_by']


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    owner = UserSerializer(read_only=True)
    cr_date = serializers.DateTimeField(read_only=True)
    due_date = serializers.DateTimeField(read_only=True)
    mark = serializers.BooleanField(read_only=True)
    list_id = ListSerializer(read_only=True)

    def create(self, validated_data):
        list = List(**validated_data)
        list.created_by = User.objects.filter.first()
        list.list_id = List.objects.filter.first()
        list.save()
        return list

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class TaskModelSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    list_id = ListSerializer(read_only=True)

    class Meta:
        model = List
        fields = ['id', 'name', 'owner', 'cd_date', 'due_date', 'mark', 'list_id']