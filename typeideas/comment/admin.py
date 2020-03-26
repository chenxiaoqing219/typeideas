from django.contrib import admin

from typeideas.custom_site import custom_site
from .models import Comment
# from typeideas.base_admin import BaseOwnerAdmin

@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')