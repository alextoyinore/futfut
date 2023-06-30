from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import *


class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class FutUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = FutUser
        fields = '__all__'
        depth = 2

class FutUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = FutUser
        fields = '__all__'
        depth = 2


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        depth = 1

class PollPostOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollPostOption
        fields = '__all__'

class PollPostResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollPostResponse
        fields = '__all__'

class QuestionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionPost
        fields = '__all__'

class QuestionPostResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionPostResponse
        fields = '__all__'

class BaseMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseMember
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = '__all__'


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'


class RepublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Republish
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
