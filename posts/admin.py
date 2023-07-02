from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author",)

admin.site.register(Post, PostAdmin)
