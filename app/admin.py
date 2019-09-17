from django.contrib import admin
from app.models import Post
from app.models import Tag, Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
