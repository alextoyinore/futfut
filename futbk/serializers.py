from rest_framework import serializers
from .models import FutUser, Geo, Address, Base, BaseMember, Bookmark, Post, Reply, Republish, Like, Follow, Message, \
    Notification, View


class FutUserSerializer(serializers.Serializer):
    class Meta:
        model = FutUser
        fields = '__all__'
        depth = 2


class GeoSerializer(serializers.Serializer):
    class Meta:
        model = Geo
        fields = '__all__'


class AddressSerializer(serializers.Serializer):
    class Meta:
        model = Address
        fields = '__all__'


class BaseSerializer(serializers.Serializer):
    class Meta:
        model = Base
        fields = '__all__'


class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields = '__all__'
        depth = 1


class BaseMemberSerializer(serializers.Serializer):
    class Meta:
        model = BaseMember
        fields = '__all__'


class ReplySerializer(serializers.Serializer):
    class Meta:
        model = Reply
        fields = '__all__'


class LikeSerializer(serializers.Serializer):
    class Meta:
        model = Like
        fields = '__all__'


class ViewSerializer(serializers.Serializer):
    class Meta:
        model = View
        fields = '__all__'


class BookmarkSerializer(serializers.Serializer):
    class Meta:
        model = Bookmark
        fields = '__all__'


class RepublishSerializer(serializers.Serializer):
    class Meta:
        model = Republish
        fields = '__all__'


class FollowSerializer(serializers.Serializer):
    class Meta:
        model = Follow
        fields = '__all__'


class MessageSerializer(serializers.Serializer):
    class Meta:
        model = Message
        fields = '__all__'


class NotificationSerializer(serializers.Serializer):
    class Meta:
        model = Notification
        fields = '__all__'

