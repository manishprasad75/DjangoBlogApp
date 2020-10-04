from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'author', 'date_posted']
    list_filter = ['author']


admin.site.register(Post, PostAdmin)
