from django.contrib import admin

from blog.models import BlogPost

# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "date_created"]
    list_editable = ["status"]