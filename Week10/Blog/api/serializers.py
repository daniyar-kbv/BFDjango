from rest_framework import serializers
from main.models import Post, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=300)
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    cr_date = serializers.DateTimeField(read_only=True)
    title = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=255)

    def create(self, validated_data):
        post = Post(**validated_data)
        post.user = User.objects.first()
        post.save()
        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.name)
        instance.save()
        return instance


class PostModelSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'user', 'cr_date', 'content']


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    cr_date = serializers.DateTimeField(read_only=True)
    content = serializers.CharField(max_length=255)
    post_id = PostSerializer(read_only=True)

    def create(self, validated_data):
        comment = Comment(**validated_data)
        comment.user = User.objects.first()
        comment.post_id = Post.objects.first()
        comment.save()
        return comment

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance


class CommentModelSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post_id = PostSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'cr_date', 'content', 'post_id']