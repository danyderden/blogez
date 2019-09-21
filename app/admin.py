from django.contrib import admin
from app.models import Tag, Comment, Post
# Register your models here.

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
