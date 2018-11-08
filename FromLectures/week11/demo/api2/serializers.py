from rest_framework import serializers
from main2.models import Student, Post, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=300)
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()
    # class Meta:
    #     model = User
    #     fields = ('id', 'username', 'email', )


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    created_by = UserSerializer(read_only=True)

    def create(self, validated_data):
        student = Student(**validated_data)
        student.created_by = User.objects.first()
        student.save()
        return student

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class StudentModelSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'created_by']


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    text = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        post_id = validated_data.pop('post_id')
        post = Post.objects.get(post_id=post_id)
        comment = Comment(**validated_data)
        comment.post = post
        comment.save()
        return comment
