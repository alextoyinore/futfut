from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

class GeoView(generics.ListCreateAPIView):
    queryset = Geo.objects.all()
    serializer_class = GeoSerializer

class GeoSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Geo.objects.all()
    serializer_class = GeoSerializer

class AddressView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class FutUserView(generics.ListCreateAPIView):
    queryset = FutUser.objects.prefetch_related('address').all()
    serializer_class = FutUserSerializer


class FutUserSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FutUser.objects.prefetch_related('address')
    serializer_class = FutUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return objects belonging to the authenticated user
        return self.queryset.filter(username=self.request.username)

    def perform_update(self, serializer):
        serializer.save(username=self.request.username)


class BaseView(generics.ListCreateAPIView):
    queryset = Base.objects.prefetch_related('user').all()
    serializer_class = BaseSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        permission_classes = []
        if self.request.method == 'GET':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        permission_classes = []
        if self.request.method == 'GET':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class PostSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.prefetch_related('user', 'base').all()
    serializer_class = PostSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method == 'GET':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


# TODO: Views for PollPostOption, PollPostResponse
# TODO: Single views for PollPostOption, PollPostResponse
# TODO: Views for QuestionPost, QuestionPostResponse
# TODO: Single views for PollPostOption, PollPostResponse


class FeedView(generics.ListAPIView):
    queryset = Post.objects.prefetch_related('user', 'base').all()
    serializer_class = PostSerializer

class ViewsView(generics.ListCreateAPIView):
    queryset = View.objects.prefetch_related('user', 'post').all()
    serializer_class = ViewSerializer

class ViewsSingleView(generics.RetrieveDestroyAPIView):
    queryset = View.objects.prefetch_related('user', 'post').all()
    serializer_class = ViewSerializer
    
    def get_permissions(self):
        permission_classes = []
        if self.request.method == 'GET':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class BookmarkView(generics.ListCreateAPIView):
    queryset = Bookmark.objects.prefetch_related('user', 'post').all()
    serializer_class = BookmarkSerializer
    
    def get_permissions(self):
        permission_classes = []
        if self.request.method == 'GET':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class BookmarkSingleView(generics.RetrieveDestroyAPIView):
    queryset = Bookmark.objects.prefetch_related('user', 'post').all()
    serializer_class = BookmarkSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method == 'GET':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class RepublishView(generics.ListCreateAPIView):
    queryset = Republish.objects.prefetch_related('user', 'post').all()
    serializer_class = RepublishSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method == 'GET':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class RepublishSingleView(generics.RetrieveDestroyAPIView):
    queryset = Republish.objects.prefetch_related('user', 'post').all()
    serializer_class = RepublishSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method == 'GET':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class FollowView(generics.ListCreateAPIView):
    queryset = Follow.objects.prefetch_related('user').all()
    serializer_class = FollowSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method == 'GET':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class FollowSingleView(generics.RetrieveDestroyAPIView):
    queryset = Follow.objects.prefetch_related('user').all()
    serializer_class = FollowSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method == 'GET':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


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
