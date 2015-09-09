from django.contrib import admin
from .models import Photo, Comment

# Register your models here.


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Comment, CommentAdmin)