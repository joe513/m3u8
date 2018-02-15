from django.contrib import admin

from app.models import Channel, Playlist, Upload


class ChannelAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'group', 'playlist', 'created_at']
    search_fields = ['title', 'group', 'path']
    list_filter = ['created_at', 'playlist', ]
    ordering = ['-created_at']


class PlaylistAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'public_key', 'public_link', ]
    list_display = ['user', 'count', 'created_at']


class UploadAdmin(admin.ModelAdmin):
    list_display = ['info', 'user', 'created_at']


admin.site.register(Channel, ChannelAdmin)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Upload, UploadAdmin)
