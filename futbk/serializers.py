from rest_framework import serializers
from .models import FutUser, Geo, Address, Base, BaseMember, Bookmark, Post, Republish, Like, Follow, Message, \
    Notification, View


class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class FutUserSerializer(serializers.ModelSerializer):
    class Meta:
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


class BaseMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseMember
        fields = '__all__'


# class ReplySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reply
#         fields = '__all__'


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

