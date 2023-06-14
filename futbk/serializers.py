from rest_framework import serializers
from .models import FutUser, Geo, Address, Base, BaseMember, Bookmark, Post, Reply, Republish, Like, Follow, Message, Notification

class FutUserSerializer(serializers.Serializer):
    class Meta:
        model = FutUser
        fields = '__all__'

class GeoSerializer(serializers.Serializer):
    class Meta:
        model = Geo
        fields = '__all__'

