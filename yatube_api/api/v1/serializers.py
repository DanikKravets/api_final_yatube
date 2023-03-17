import base64

from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post, User


class Base64ImageField(serializers.ImageField):
    """Serializer for processing images uploaded in base64."""
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class PostSerializer(serializers.ModelSerializer):
    """Post Serializer"""
    author = SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    image = Base64ImageField(
        required=False,
        allow_null=True,
    )

    class Meta:
        fields = ('id', 'text', 'pub_date', 'author', 'group', 'image')
        model = Post
        read_only_fields = ('id', 'pub_date', 'author')


class CommentSerializer(serializers.ModelSerializer):
    """Comment Serializer"""
    author = SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    post = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'post', 'created')


class FollowSerializer(serializers.ModelSerializer):
    """Follow Serializer"""

    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    following = serializers.SlugRelatedField(
        slug_field='username',
        read_only=False,
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        fields = ('id', 'user', 'following')
        validators = (
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message="You are already following this author",
            ),
        )

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError(
                "You can't follow yourself"
            )
        return data


class GroupSerializer(serializers.ModelSerializer):
    """Group Serializer"""

    class Meta:
        model = Group
        fields = ('id', 'title', 'description', 'slug')
