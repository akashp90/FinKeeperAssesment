from django.contrib import admin
from .models import Post, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'created_at')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)