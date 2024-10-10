from django.contrib import admin
from .models import Post, Like, Follow, Comment

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "date_created", "date_modified"]
    list_filter = ["date_created"]
    search_fields = ["title", "author", "description"]
    readonly_fields = ["date_created", "date_modified"]
    ordering = ('-date_created',)
    list_per_page = 25  
    
    
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "date_created"]
    search_fields = ["user", "post"]
    readonly_fields = ["date_created"]
    ordering = ("-date_created",)
    list_per_page = 50
    

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ["follower", "following", "date_created"]
    search_fields = ["follower", "following"]
    readonly_fields = ["date_created",]
    ordering = ("-date_created",)
    list_per_page = 50    
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["title", "post", "author"]
    search_fields = ["author"]
    readonly_fields = ["author", "post", "date_created"]
    ordering = ("-date_created",)
    list_per_page = 50    
    