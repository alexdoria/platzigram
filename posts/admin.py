from django.contrib import admin
from posts.models import Post

# Register your models here.
# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """List the fields you want to see"""
    list_display = ('user', 'title', 'post', 'date_created')
    list_display_links = ('title', 'post')
