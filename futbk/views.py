from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics


# Create your views here.

class FutUserView(generics.ListCreateAPIView):
    queryset = FutUser.objects.prefetch_related('address').all()
    serializer_class = FutUserSerializer


class FutUserSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FutUser.objects.prefetch_related('address').get()
    serializer_class = FutUserSerializer


class BaseView(generics.ListCreateAPIView):
    queryset = Base.objects.prefetch_related('user').all()
    serializer_class = BaseSerializer


class BaseSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Base.objects.prefetch_related('user').get()
    serializer_class = BaseSerializer


class BaseMemberView(generics.ListCreateAPIView):
    queryset = BaseMember.objects.prefetch_related('user').all()
    serializer_class = BaseMemberSerializer


class BaseMemberSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BaseMember.objects.prefetch_related('user').get()
    serializer_class = BaseMemberSerializer


class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.prefetch_related('user', 'base').all()
    serializer_class = PostSerializer


class PostSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.prefetch_related('user', 'base').get()
    serializer_class = PostSerializer


class ReplyView(generics.ListCreateAPIView):
    queryset = Reply.objects.prefetch_related('user', 'post').all()
    serializer_class = ReplySerializer


class ReplySingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.prefetch_related('user', 'post').get()
    serializer_class = ReplySerializer


class ViewsView(generics.ListCreateAPIView):
    queryset = View.objects.prefetch_related('user', 'post').all()
    serializer_class = ViewSerializer


class ViewsSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = View.objects.prefetch_related('user', 'post').get()
    serializer_class = ViewSerializer


class BookmarkView(generics.ListCreateAPIView):
    queryset = Bookmark.objects.prefetch_related('user', 'post').all()
    serializer_class = BookmarkSerializer


class BookmarkSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bookmark.objects.prefetch_related('user', 'post').get()
    serializer_class = BookmarkSerializer


class RepublishView(generics.ListCreateAPIView):
    queryset = Republish.objects.prefetch_related('user', 'post').all()
    serializer_class = RepublishSerializer


class RepublishSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Republish.objects.prefetch_related('user', 'post').get()
    serializer_class = RepublishSerializer


class FollowView(generics.ListCreateAPIView):
    queryset = Follow.objects.prefetch_related('user').all()
    serializer_class = FollowSerializer


class FollowSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Follow.objects.prefetch_related('user').get()
    serializer_class = FollowSerializer


class MessageView(generics.ListCreateAPIView):
    queryset = Message.objects.prefetch_related('user').all()
    serializer_class = MessageSerializer


class MessageSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.prefetch_related('user').get()
    serializer_class = MessageSerializer


class NotificationView(generics.ListCreateAPIView):
    queryset = Notification.objects.prefetch_related('user').all()
    serializer_class = NotificationSerializer


class NotificationSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.prefetch_related('user').get()
    serializer_class = NotificationSerializer
