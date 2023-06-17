from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics

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


class BaseSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Base.objects.prefetch_related('user')
    serializer_class = BaseSerializer


class BaseMemberView(generics.ListCreateAPIView):
    queryset = BaseMember.objects.prefetch_related('user').all()
    serializer_class = BaseMemberSerializer


class BaseMemberSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BaseMember.objects.prefetch_related('user')
    serializer_class = BaseMemberSerializer


class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.prefetch_related('user', 'base').all()
    serializer_class = PostSerializer


class PostSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.prefetch_related('user', 'base')
    serializer_class = PostSerializer


class FeedView(generics.ListAPIView):
    queryset = Post.objects.prefetch_related('user', 'base')
    serializer_class = PostSerializer


# class ReplyView(generics.ListCreateAPIView):
#     queryset = Reply.objects.prefetch_related('user', 'post').all()
#     serializer_class = ReplySerializer
#
#
# class ReplySingleView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Reply.objects.prefetch_related('user', 'post')
#     serializer_class = ReplySerializer


class ViewsView(generics.ListCreateAPIView):
    queryset = View.objects.prefetch_related('user', 'post').all()
    serializer_class = ViewSerializer


class ViewsSingleView(generics.RetrieveDestroyAPIView):
    queryset = View.objects.prefetch_related('user', 'post')
    serializer_class = ViewSerializer


class BookmarkView(generics.ListCreateAPIView):
    queryset = Bookmark.objects.prefetch_related('user', 'post').all()
    serializer_class = BookmarkSerializer


class BookmarkSingleView(generics.RetrieveDestroyAPIView):
    queryset = Bookmark.objects.prefetch_related('user', 'post')
    serializer_class = BookmarkSerializer


class RepublishView(generics.ListCreateAPIView):
    queryset = Republish.objects.prefetch_related('user', 'post').all()
    serializer_class = RepublishSerializer


class RepublishSingleView(generics.RetrieveDestroyAPIView):
    queryset = Republish.objects.prefetch_related('user', 'post')
    serializer_class = RepublishSerializer


class FollowView(generics.ListCreateAPIView):
    queryset = Follow.objects.prefetch_related('user').all()
    serializer_class = FollowSerializer


class FollowSingleView(generics.RetrieveDestroyAPIView):
    queryset = Follow.objects.prefetch_related('user')
    serializer_class = FollowSerializer


class MessageView(generics.ListCreateAPIView):
    queryset = Message.objects.prefetch_related('user').all()
    serializer_class = MessageSerializer


class MessageSingleView(generics.RetrieveDestroyAPIView):
    queryset = Message.objects.prefetch_related('user')
    serializer_class = MessageSerializer


class NotificationView(generics.ListCreateAPIView):
    queryset = Notification.objects.prefetch_related('user').all()
    serializer_class = NotificationSerializer


class NotificationSingleView(generics.RetrieveDestroyAPIView):
    queryset = Notification.objects.prefetch_related('user')
    serializer_class = NotificationSerializer

