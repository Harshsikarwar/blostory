from django.contrib import admin
from .models import BlogPost
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "create_at", "update_at")


admin.site.register(BlogPost, BlogPostAdmin)