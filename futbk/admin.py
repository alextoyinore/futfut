from django.contrib import admin
from .models import *


# Register your models here.

class FutUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'tag_line', 'occupation', 'gender', 'activated',
                    'address']
    search_fields = ('username', 'first_name')


class GeoAdmin(admin.ModelAdmin):
    list_display = ['id', 'lat', 'long']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'country', 'state', 'zip_code', 'geo']
    search_fields = ('country', 'zip_code')


class BaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'date']
    search_fields = 'title'


class BaseMemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'base']


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'user', 'base', 'date']
    search_fields = ('text', 'user')


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'user', 'post']
    search_fields = 'text'


class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'date']


class ViewAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'ip_address', 'date']


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'date']


class RepublishAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'date']


class FollowAdmin(admin.ModelAdmin):
    list_display = ['id', 'follower', 'followed', 'date']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'sender', 'reciever', 'date']
    search_fields = ('title', 'text')


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'sender', 'date']
    search_fields = ('title', 'sender', 'text')
