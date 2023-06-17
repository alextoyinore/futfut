from django.contrib import admin
from .models import *


# Register your models here.

class FutUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'tag_line', 'occupation', 'gender', 'activated',
                    'address']
    search_fields = ('username', 'first_name')


admin.site.register(FutUser, FutUserAdmin)


class GeoAdmin(admin.ModelAdmin):
    list_display = ['id', 'lat', 'long']


admin.site.register(Geo, GeoAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'country', 'state', 'zip_code', 'geo']
    search_fields = ('country', 'zip_code')


admin.site.register(Address, AddressAdmin)


class BaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'date']
    search_fields = ('title',)


admin.site.register(Base, BaseAdmin)


class BaseMemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'base']


admin.site.register(BaseMember, BaseMemberAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'user', 'base', 'date']
    search_fields = ('text', 'user')


admin.site.register(Post, PostAdmin)


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'user', 'post']
    search_fields = ('text',)


# admin.site.register(Reply, ReplyAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'date']


admin.site.register(Like, LikeAdmin)


class ViewAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'ip_address', 'date']


admin.site.register(View, ViewAdmin)


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'date']


admin.site.register(Bookmark, BookmarkAdmin)


class RepublishAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'date']


admin.site.register(Republish, RepublishAdmin)


class FollowAdmin(admin.ModelAdmin):
    list_display = ['id', 'follower', 'followed', 'date']


admin.site.register(Follow, FollowAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'msg_sender', 'msg_receiver', 'date']
    search_fields = ('title', 'text')


admin.site.register(Message, MessageAdmin)


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'sender', 'date']
    search_fields = ('title', 'sender', 'text')


admin.site.register(Notification, NotificationAdmin)
