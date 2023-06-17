from django.urls import path
from .views import *

# Creating paths here


urlpatterns = [
    path('base/', BaseView.as_view(), name='bases'),
    path('base/<int:pk>', BaseSingleView.as_view(), name='base'),

    # base member endpoints
    path('base-member/', BaseMemberView.as_view(), name='base-members'),
    path('base-member/<int:pk>', BaseMemberSingleView.as_view(), name='base-member'),

    # post endpoints
    path('post/', PostView.as_view(), name='posts'),
    path('post/<int:pk>', PostSingleView.as_view(), name='post'),

    # feed endpoints
    path('feed/', FeedView.as_view(), name='feeds'),

    # reply endpoints
    # path('reply/', ReplyView.as_view(), name='replies'),
    # path('reply/<int:id>', ReplySingleView.as_view(), name='reply'),

    # views endpoints
    path('view/', ViewsView.as_view(), name='views'),
    path('view/<int:pk>', ViewsSingleView.as_view(), name='view'),

    # bookmark endpoints
    path('bookmark/', BookmarkView.as_view(), name='bookmarks'),
    path('bookmark/<int:pk>', BookmarkSingleView.as_view(), name='bookmark'),

    # republish endpoints
    path('republish/', RepublishView.as_view(), name='republishes'),
    path('republish/<int:pk>', RepublishSingleView.as_view(), name='republish'),

    # follow endpoints
    path('follow/', FollowView.as_view(), name='follows'),
    path('follow/<int:pk>', FollowSingleView.as_view(), name='follow'),

    # message endpoints
    path('message/', MessageView.as_view(), name='messages'),
    path('message/<int:pk>', MessageSingleView.as_view(), name='message'),

    # notifications endpoints
    path('notification/', NotificationView.as_view(), name='notifications'),
    path('notification/<int:pk>', NotificationSingleView.as_view(), name='notification'),
]

