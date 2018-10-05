from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'cr_date', 'title', 'content')
    list_display_links = ('id', 'author', 'cr_date', 'title', 'content')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'cr_date', 'content', 'post_id')
    list_display_links = ('id', 'author', 'cr_date', 'content', 'post_id')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)