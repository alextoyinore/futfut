from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

class FutUserView(generics.ListCreateAPIView):
    queryset = FutUser.objects.prefetch_related('address').all()
    serializer_class = FutUserSerializer


class FutUserSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FutUser.objects.prefetch_related('address')
    serializer_class = FutUserSerializer


class BaseView(generics.ListCreateAPIView):
    queryset = Base.objects.prefetch_related('user').all()
    serializer_class = BaseSerializer
    permission_classes = [IsAuthenticated]


class BaseSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Base.objects.prefetch_related('user').all()
    serializer_class = BaseSerializer
    permission_classes = [IsAuthenticated]


class BaseMemberView(generics.ListCreateAPIView):
    queryset = BaseMember.objects.prefetch_related('user').all()
    serializer_class = BaseMemberSerializer
    permission_classes = [IsAuthenticated]


class BaseMemberSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BaseMember.objects.prefetch_related('user').all()
    serializer_class = BaseMemberSerializer
    permission_classes = [IsAuthenticated]


class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.prefetch_related('user', 'base').all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]


class PostSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.prefetch_related('user', 'base').all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class FeedView(generics.ListAPIView):
    queryset = Post.objects.prefetch_related('user', 'base').all()
    serializer_class = PostSerializer


class ViewsView(generics.ListCreateAPIView):
    queryset = View.objects.prefetch_related('user', 'post').all()
    serializer_class = ViewSerializer


class ViewsSingleView(generics.RetrieveDestroyAPIView):
    queryset = View.objects.prefetch_related('user', 'post').all()
    serializer_class = ViewSerializer
    permission_classes = [IsAuthenticated]


class BookmarkView(generics.ListCreateAPIView):
    queryset = Bookmark.objects.prefetch_related('user', 'post').all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]


class BookmarkSingleView(generics.RetrieveDestroyAPIView):
    queryset = Bookmark.objects.prefetch_related('user', 'post').all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]


class RepublishView(generics.ListCreateAPIView):
    queryset = Republish.objects.prefetch_related('user', 'post').all()
    serializer_class = RepublishSerializer
    permission_classes = [IsAuthenticated]


class RepublishSingleView(generics.RetrieveDestroyAPIView):
    queryset = Republish.objects.prefetch_related('user', 'post').all()
    serializer_class = RepublishSerializer
    permission_classes = [IsAuthenticated]


class FollowView(generics.ListCreateAPIView):
    queryset = Follow.objects.prefetch_related('user').all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]


class FollowSingleView(generics.RetrieveDestroyAPIView):
    queryset = Follow.objects.prefetch_related('user').all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]


class MessageView(generics.ListCreateAPIView):
    queryset = Message.objects.prefetch_related('user').all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]


class MessageSingleView(generics.RetrieveDestroyAPIView):
    queryset = Message.objects.prefetch_related('user').all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]


class NotificationView(generics.ListCreateAPIView):
    queryset = Notification.objects.prefetch_related('user').all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAdminUser]


class NotificationSingleView(generics.RetrieveDestroyAPIView):
    queryset = Notification.objects.prefetch_related('user').all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

